
from django.shortcuts import render
from rest_framework.views import APIView
from HRproj.util.Mail.HR_Workflow_Emails import EmailUtils
from jobpost.models.jobpostapprovalmodel import JobPostApproval

from jobpost.models.jobpostmodel import JobPost
from jobpost.serializers import  JobPostApprovalSerializer, JobPostDetailsPostSerializer
from django.http.response import JsonResponse
from rest_framework import status  
from rest_framework.response import Response
from datetime import datetime
from django.contrib.auth.models import User, Group
from django.db import transaction

from managestages.models import Stage
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

# Create your views here.

class JobPostApi(APIView):

    

    def put(self, request, format=None): 
        try:
            with transaction.atomic():        
                jobpost =  JobPost.objects.get(JobPostId=request.data['JobPostId'])
                # jobpost.ModifiedBy = ""
                jobpost.ModifiedOn = datetime.now()
                jobpost.ModifiedBy = request.data['UserName']
                JobPostDetailsPost_serializer = JobPostDetailsPostSerializer(jobpost ,data=request.data)
                if JobPostDetailsPost_serializer.is_valid():
                    jobpost1 = JobPostDetailsPost_serializer.save()
                    if jobpost1 is not None:
                        success = self.insertorupdatejobpostapproval(jobpost1, request.data)
                        if success == True:
                            # send email to business head.

                            # body = render_to_string('businessheadjobpostapproval_template.html', context)
                            
                            BHUserName =  request.data["BH_User_Name"]       
                            BHuser = User.objects.get(username=BHUserName)
                            subject = 'Action: Job Post- '+jobpost1.JobCode+' awaiting for approval'
                            context = {
                                'jobcode': jobpost1.JobCode,
                                'hiringmanager' : jobpost1.LastName+", "+jobpost1.FirstName,
                                'url' : settings.APP_URL,
                                'approvername' : BHuser.last_name+", "+BHuser.first_name
                            }
                            body = EmailUtils.getEmailBody('businessheadjobpostapproval_template.html', context)
                            print(body)
                            print(subject)
                            print(BHuser.email)
                            print(jobpost1.Email)
                            # send_mail(
                            #     subject,
                            #     message=body,
                            #     recipient_list=[BHuser.email],
                            #     from_email=settings.DEFAULT_FROM_EMAIL,
                            #     fail_silently=False,
                            # )  
                            # if settings.SEND_EMAIL:    
                            #     email = EmailMessage(
                            #                 subject=subject,
                            #                 body=body,
                            #                 from_email=settings.DEFAULT_FROM_EMAIL,
                            #                 to=[BHuser.email],            
                            #                 cc=[jobpost1.Email]
                            #     )

                            #     email.content_subtype = "html"  # set the content subtype to html
                            #     email.send()   
                            EmailUtils.sendEmail(subject, body, [BHuser.email], [jobpost1.Email])                               
                    return Response(Messages1.UPD_SCFL)
                return Response(JobPostDetailsPost_serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        except Exception as exp:
            # exp.with_traceback()
            return Response(Messages1.ERR_CRTG_JP+str(exp), status=status.HTTP_400_BAD_REQUEST)        

    # @transaction.atomic
    def post(self, request, format=None):
        # company_data = JSONParser().parse(request)
        try:
            with transaction.atomic():
                JobPostDetailsPost_serializer = JobPostDetailsPostSerializer(data=request.data)    
                if JobPostDetailsPost_serializer.is_valid():
                    jobpost1 = JobPostDetailsPost_serializer.save()
                    if jobpost1 is not None:                             
                        success = self.insertorupdatejobpostapproval(jobpost1, request.data)
                        if success == True:
                            # send email to business head.

                            # body = render_to_string('businessheadjobpostapproval_template.html', context)
                            
                            BHUserName =  request.data["BH_User_Name"]       
                            BHuser = User.objects.get(username=BHUserName)
                            subject = 'Action: Job Post- '+jobpost1.JobCode+' awaiting for approval'
                            context = {
                                'jobcode': jobpost1.JobCode,
                                'hiringmanager' : jobpost1.LastName+", "+jobpost1.FirstName,
                                'url' : settings.APP_URL,
                                'approvername' : BHuser.last_name+", "+BHuser.first_name
                            }
                            body = EmailUtils.getEmailBody('businessheadjobpostapproval_template.html', context)
                            print(body)
                            print(subject)
                            print(BHuser.email)
                            print(jobpost1.Email)
                            # send_mail(
                            #     subject,
                            #     message=body,
                            #     recipient_list=[BHuser.email],
                            #     from_email=settings.DEFAULT_FROM_EMAIL,
                            #     fail_silently=False,
                            # )  
                            # if settings.SEND_EMAIL:    
                            #     email = EmailMessage(
                            #                 subject=subject,
                            #                 body=body,
                            #                 from_email=settings.DEFAULT_FROM_EMAIL,
                            #                 to=[BHuser.email],            
                            #                 cc=[jobpost1.Email]
                            #     )

                            #     email.content_subtype = "html"  # set the content subtype to html
                            #     email.send()                      
                            EmailUtils.sendEmail(subject, body, [BHuser.email], [jobpost1.Email])
                    # return Response({"status": "success", "data": company_serializer.data}, status=status.HTTP_200_OK)  
                            return Response(Messages1.JP_CRTD_SCFL, status=status.HTTP_200_OK)
                        else:
                            return Response(Messages1.JP_CRTN_FAIL, status=status.HTTP_400_BAD_REQUEST)   
                return Response(JobPostDetailsPost_serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
        except Exception as exp:
            # exp.with_traceback()
            return Response(Messages1.ERR_CRTG_JP+str(exp), status=status.HTTP_400_BAD_REQUEST)
        # return Response("Exception while creation Job Post", status=status.HTTP_400_BAD_REQUEST)

    def insertorupdatejobpostapproval(self, jobpost1, data):
        success = True
        try:
            BHUserName =  data["BH_User_Name"]
            HRUserName =  data["HR_User_Name"]

            BHuser = User.objects.get(username=BHUserName)
            BHstage = Stage.objects.filter(StageName=Constants1.STAGE_BHA).first()
            BHrole = Group.objects.filter(name=Constants1.ROLE_BH).first()

            HRuser = User.objects.get(username=HRUserName)
            HRstage = Stage.objects.filter(StageName=Constants1.STAGE_PP).first()
            HRrole = Group.objects.filter(name=Constants1.ROLE_HR).first()  
            if (BHuser is not None and BHstage is not None and BHrole is not None):
                jobpostapprovalBH = JobPostApproval.objects.filter(jobpost= jobpost1, Stage=BHstage, role=BHrole).first()
                if jobpostapprovalBH is not None:
                    jobpostapprovalreturn = JobPostApproval.objects.filter(jobpost= jobpost1, Stage=BHstage, role=BHrole).update(
                    # jobPostApprovalId = jobpostapprovalBH.jobPostApprovalId,    
                    jobpost = jobpost1,
                    approverName =  BHuser.username,
                    FirstName = BHuser.first_name,
                    LastName = BHuser.last_name,
                    Email = BHuser.email,
                    Stage = BHstage,
                    role = BHrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
                else:
                    jobpostapprovalreturn = JobPostApproval.objects.create(
                    jobpost = jobpost1,
                    approverName =  BHuser.username,
                    FirstName = BHuser.first_name,
                    LastName = BHuser.last_name,
                    Email = BHuser.email,
                    Stage = BHstage,
                    role = BHrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())         

            if (HRuser is not None and HRstage is not None and HRrole is not None):
                jobpostapprovalHR = JobPostApproval.objects.filter(jobpost= jobpost1, Stage=HRstage, role=HRrole).first()
                if jobpostapprovalHR is not None:
                    jobpostapprovalreturn = JobPostApproval.objects.filter(jobpost= jobpost1, Stage=HRstage, role=HRrole).update(
                    jobpost = jobpost1,
                    approverName =  HRuser.username,
                    FirstName = HRuser.first_name,
                    LastName = HRuser.last_name,
                    Email = HRuser.email,
                    Stage = HRstage,
                    role = HRrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
                else:
                    jobpostapprovalreturn = JobPostApproval.objects.create(
                    jobpost = jobpost1,
                    approverName =  HRuser.username,
                    FirstName = HRuser.first_name,
                    LastName = HRuser.last_name,
                    Email = HRuser.email,
                    Stage = HRstage,
                    role = HRrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
        except:
            success = False
            raise Exception (Messages1.ERR_SAVE_APP_DATA)
        return success