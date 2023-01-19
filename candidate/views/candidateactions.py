from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from candidate.models.candidateactionmodel import CandidateActionModel
from candidate.serializers import AddFeedBackSerializer, AddSelectedCandidatesSerializer, CandidateActionModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from django.db import transaction
from candidate.models.candidatemodel import Candidate
from candidate.models.candidateapprovalmodel import CandidateApprovalModel
from datetime import datetime
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1
from managestages.models import Stage
from django.contrib.auth.models import User, Group
from jobpost.models.jobpostuserrolesmodel import JobPostUserRolesModel
from HRproj.util.Mail.HR_Workflow_Emails import EmailUtils
from django.conf import settings
from jobpost.models.jobpoststakeholders import JobPostStakeHolders
from candidate.models.selected_Candidates_Model import Selected_Candidates



class CandidateAction(ModelViewSet):
    @action(detail=True, methods=['post'])
    def candidateactiondetails(self, request, format=None):
        print(request.data)
        CandidateActionModel1 = CandidateActionModel.objects.filter(
            ApproverName=request.data["ApproverName"])
        CandidateActionModel_serializer = CandidateActionModelSerializer(
            CandidateActionModel1, many=True)
        return Response(CandidateActionModel_serializer.data)

    @action(detail=True, methods=['post'])
    def candidateworkflowsubmit(self, request, format=None):
        try:
            with transaction.atomic():
                candidateapprovalid = request.data["candidateapprovalid"]
                candidateid = request.data["candidateid"]
                Status = request.data["status"]
                comments = request.data["comments"]
                feedback=None
                feedback = request.data["feedback"]
                response = ''
                candidateob = Candidate.objects.filter(
                    CandidateId=candidateid).first()
                
                ca = CandidateApprovalModel.objects.filter(CandidateApprovalId=candidateapprovalid).update(
                    approvalStatus=Status,
                    approvalDate=datetime.now(),
                    approvalComments=comments
                )
                
                # candidate = Candidate.objects.filter(CandidateId=candidateid).first()
                emails = JobPostStakeHolders.objects.filter(JobPostId=candidateob.Jobpost.JobPostId).first()
                HRemail,HRname,FCemail,FCname,GMemail,GMname=EmailUtils.getRoles(candidateid=candidateob.CandidateId)
                
                if ca is not None:
                    if (Status == Constants1.SELECT_FOR_INTERVIEW):
                        # EmailUtils.getRoles(candidateid=candidateob.CandidateId)

                        hiringmanagermail = emails.HMemail
                        recruitermail = emails.RecruiterEmail
                        subject = 'Candidate'+candidateob.CandidateCode+'selected for interview'
                        context = {
                            'CandidateCode': candidateob.CandidateCode,
                            'hiringmanager' : emails.HMname,
                            'recruiter' : emails.RecruiterName,
                            'url' : settings.APP_URL,
                        }
                        body = EmailUtils.getEmailBody('HiringManager_Interview_template.html', context)
                        print(body)
                        print(subject)
                        print(hiringmanagermail)
                        EmailUtils.sendEmail(subject, body, [hiringmanagermail], [recruitermail])


                        stage = Stage.objects.filter(
                            StageName=Constants1.STAGE_CI).first()
                        response = Messages1.CAN_IP

                    elif (Status == Constants1.HM_SHORTLISTED):
                        
                        EmailUtils.getRoles(candidateid=candidateob.CandidateId)

                        hiringmanagermail = emails.HMemail
                        recruitermail = emails.RecruiterEmail
                        subject = 'Candidate'+candidateob.CandidateCode+'shortlisted in interview'
                        context = {
                            'CandidateCode': candidateob.CandidateCode,
                            'hiringmanager' : emails.HMname,
                            'recruitername' : emails.RecruiterName,
                            'url' : settings.APP_URL,
                        }
                        body = EmailUtils.getEmailBody('Candidate_ShortlistedforHRInterview_template.html', context)
                        print(body)
                        print(subject)
                        print(recruitermail)
                        EmailUtils.sendEmail(subject, body, [recruitermail], [hiringmanagermail])

                        stage = Stage.objects.filter(
                            StageName=Constants1.STAGE_HR_INTERVIEW).first()
                        response = "Candidate has been shortlisted for HR interview "

                    elif (Status == Constants1.BH_CANDIDATE_APPROVAL):

                        EmailUtils.getRoles(candidateid=candidateob.CandidateId)
                        hiringmanagermail = emails.HMemail
                        businessheadmail = emails.BHemail
                        HRmail = HRemail
                        recruitermail = emails.RecruiterEmail
                        subject = 'Candidate' +candidateob.CandidateCode+ ' approved by BH'
                        context = {
                            'CandidateCode': candidateob.CandidateCode,
                            'businesshead':emails.BHname,
                            'hiringmanager' : emails.HMname,
                            'recruitername' : emails.RecruiterName,                                
                            'url' : settings.APP_URL,
                        }   
                        body = EmailUtils.getEmailBody('BusinessHead_Can_Approval_template.html', context)
                        print(body)
                        print(subject)
                        print(businessheadmail)
                        EmailUtils.sendEmail(subject, body, [businessheadmail], [hiringmanagermail,recruitermail, HRmail])

                        stage = Stage.objects.filter(
                            StageName=Constants1.STAGE_FC_Approval).first()
                        success = self.insertnewrow(candidateob, Status)
                        if success == False:
                            raise Exception(
                                "error while creating new row in candidate approval table")
                        else:
                            response = "Candidate has been put on hold"

                        response = "Business Head has been Approved Succesfully"
                    elif (Status == Constants1.FC_Approval):

                        EmailUtils.getRoles(candidateid=candidateob.CandidateId)
                        hiringmanagermail = emails.HMemail
                        fincancecontrollermail = FCemail
                        HRmail = HRemail
                        recruitermail = emails.RecruiterEmail
                        subject = 'Candidate' +candidateob.CandidateCode+ ' approved by FC'
                        context = {
                            'CandidateCode': candidateob.CandidateCode,
                            'financecontroller':FCname,
                            'hiringmanager' : emails.HMname,
                            'recruitername' : emails.RecruiterName,                                
                            'url' : settings.APP_URL,
                        }   
                        body = EmailUtils.getEmailBody('FC_Can_Approval_template.html', context)
                        print(body)
                        print(subject)
                        print(fincancecontrollermail)
                        EmailUtils.sendEmail(subject, body, [fincancecontrollermail], [hiringmanagermail,recruitermail,HRemail])

                        stage = Stage.objects.filter(
                            StageName=Constants1.STAGE_GM_Approval).first()
                        response = "Finance Controller has been Approved Succesfully"

                    elif (Status == Constants1.GM_Approval):

                        EmailUtils.getRoles(candidateid=candidateob.CandidateId)
                        hiringmanagermail = emails.HMemail
                        generalmanagermail = GMemail
                        HRmail = HRemail
                        recruitermail = emails.RecruiterEmail
                        subject = 'Candidate' +candidateob.CandidateCode+ ' approved by GM'
                        context = {
                            'CandidateCode': candidateob.CandidateCode,
                            'generalmanager': GMname,
                            'hiringmanager' : emails.HMname,
                            'recruitername' : emails.RecruiterName,                                
                            'url' : settings.APP_URL,
                        }   
                        body = EmailUtils.getEmailBody('GM_Can_Approval_template.html', context)
                        print(body)
                        print(subject)
                        print(generalmanagermail)
                        EmailUtils.sendEmail(subject, body, [generalmanagermail], [hiringmanagermail,recruitermail,HRemail])
                        stage = Stage.objects.filter(
                            StageName=Constants1.STAGE_SELECTED).first()
                        self.addselectedcandidate(candidateob)
                        response = "Candidate has been selected"

                    elif (Status == Constants1.HR_SHORTLISTED):

                        EmailUtils.getRoles(candidateid=candidateob.CandidateId)

                        hiringmanagermail = emails.HMemail
                        businessheadmail = emails.BHemail
                        recruitermail = emails.RecruiterEmail
                        subject = 'Candidate'+candidateob.CandidateCode+'shortlisted in HR interview'
                        context = {
                            'CandidateCode': candidateob.CandidateCode,
                            'businesshead': emails.BHname,
                            'hiringmanager' : emails.HMname,
                            'recruitername' : emails.RecruiterName,
                            'url' : settings.APP_URL,
                        }
                        body = EmailUtils.getEmailBody('Candidate_SelectedAt_HR_Interview_template.html', context)
                        print(body)
                        print(subject)
                        print(recruitermail)
                        EmailUtils.sendEmail(subject, body, [businessheadmail], [recruitermail, hiringmanagermail])
                        
                        stage = Stage.objects.filter(
                            StageName=Constants1.STAGE_BH_CANDIDATE_APPROVAL).first()
                        response = "HR shortlisted Succesfully"

                    elif (Status == Constants1.HM_HOLD):
                        
                        EmailUtils.getRoles(candidateid=candidateob.CandidateId)

                        hiringmanagermail = emails.HMemail
                        recruitermail = emails.RecruiterEmail
                        subject = 'Candidate' +candidateob.CandidateCode+ ' on hold'
                        context = {
                            'CandidateCode': candidateob.CandidateCode,
                            'hiringmanager' : emails.HMname,
                            'recruitername' : emails.RecruiterName,                                  
                            'url' : settings.APP_URL,
                        }   
                        body = EmailUtils.getEmailBody('Candidate_Hold_at_Interview_template.html', context)
                        print(body)
                        print(subject)
                        print(recruitermail)
                        EmailUtils.sendEmail(subject, body, [recruitermail], [hiringmanagermail])
                            
                        stage = Stage.objects.filter(
                            StageName=Constants1.STAGE_HM_HOLD).first()
                        success = self.insertnewrow(candidateob, Status)
                        if success == False:
                            raise Exception(
                                "error while creating new row in candidate approval table")
                        else:
                            response = "Candidate has been put on hold"
                    elif (Status == Constants1.HR_HOLD):
                        stage = Stage.objects.filter(
                            StageName=Constants1.STAGE_HR_HOLD).first()
                        success = self.insertnewrow(candidateob, Status)
                        if success == False:
                            raise Exception(
                                "error while creating new row in candidate approval table")
                        else:
                            response = "Candidate has been put on  HR hold"
                    elif (Status == Constants1.REJECTED):

                        EmailUtils.getRoles(candidateid=candidateob.CandidateId)

                        hiringmanagermail = emails.HMemail
                        recruitermail = emails.RecruiterEmail
                        subject = 'Candidate' +candidateob.CandidateCode+ ' rejected'
                        context = {
                            'CandidateCode': candidateob.CandidateCode,
                            'hiringmanager' : emails.HMname,
                            'recruitername' : emails.RecruiterName,                                
                            'url' : settings.APP_URL,
                        }   
                        body = EmailUtils.getEmailBody('Candidate_Rejected_at_Interview_template.html', context)
                        print(body)
                        print(subject)
                        print(recruitermail)
                        EmailUtils.sendEmail(subject, body, [recruitermail], [hiringmanagermail])
                        
                        stage = Stage.objects.filter(
                            StageName=Constants1.STAGE_REJECTED).first()
                        response = "Candidate has been rejected"

                    elif (Status == Constants1.FURTHERREVIEW):

                        EmailUtils.getRoles(candidateid=candidateob.CandidateId)

                        hiringmanagermail = emails.HMemail
                        recruitermail = emails.RecruiterEmail
                        subject = 'Candidate' +candidateob.CandidateCode+ ' further review'
                        context = {
                            'CandidateCode': candidateob.CandidateCode,
                            'hiringmanager' : emails.HMname,
                            'recruitername' : emails.RecruiterName,                                
                            'url' : settings.APP_URL,
                        }   
                        body = EmailUtils.getEmailBody('Candidate_FurtherReviewAtInterview_template.html', context)
                        print(body)
                        print(subject)
                        print(recruitermail)
                        EmailUtils.sendEmail(subject, body, [recruitermail], [hiringmanagermail])
                        
                        stage = Stage.objects.filter(
                            StageName=Constants1.STAGE_FURTHERREVIEW).first()
                        success = self.insertnewrow(candidateob, Status)
                        if success == False:
                            raise Exception(
                                "error while creating new row in candidate approval table")
                        else:
                            response = "Candidate has been shortlisted for further review"
                    candidatecount = Candidate.objects.filter(CandidateId=candidateid).update(
                        Stage=stage
                    )
                else:
                    raise Exception
                if feedback is not None:
                    print("create bulk insert")
                    print(request.data)
                    serializer = AddFeedBackSerializer(data=feedback,many=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                return Response(response, status=status.HTTP_200_OK)
        except Exception as exp:
            return Response(Messages1.ERR_FBK_CAN+str(exp), status=status.HTTP_400_BAD_REQUEST)
    def insertnewrow(self, candidate1, status):
        success = True
        try:
            HMUserName = candidate1.Jobpost.UserName
            HRUserName = ""
            HRUserObj = JobPostUserRolesModel.objects.filter(
                RoleName=Constants1.ROLE_HR).first()
            if HRUserObj is not None:
                HRUserName = HRUserObj.UserName
            else:
                HRUserName = ""
            HRuser = User.objects.get(username=HRUserName)
            HRHoldstage = Stage.objects.filter(
                StageName=Constants1.STAGE_HR_HOLD).first()
            HRrole = Group.objects.filter(name=Constants1.ROLE_HR).first()
            HMUser = User.objects.get(username=HMUserName)
            HMHoldstage = Stage.objects.filter(
                StageName=Constants1.STAGE_HM_HOLD).first()
            HMFurtherReviewstage = Stage.objects.filter(
                StageName=Constants1.STAGE_FURTHERREVIEW).first()
            HMrole = Group.objects.filter(name=Constants1.ROLE_HM).first()


             # Finannce Controller
            FCUserObj =  JobPostUserRolesModel.objects.filter(RoleName = Constants1.ROLE_FC).first()
            if FCUserObj is not None:
                FCUserName = FCUserObj.UserName
            else:
                FCUserName = ""  
            # General Manager
            GMUserObj =  JobPostUserRolesModel.objects.filter(RoleName = Constants1.ROLE_GM).first()
            if GMUserObj is not None:
                GMUserName = GMUserObj.UserName
            else:
                GMUserName = ""  

            GMuser = User.objects.get(username=GMUserName)
            GMApprovalstage = Stage.objects.filter(StageName=Constants1.STAGE_GMA).first()
            GMrole = Group.objects.filter(name=Constants1.ROLE_GM).first() 

            FCuser = User.objects.get(username=FCUserName)
            FCApprovalstage = Stage.objects.filter(StageName=Constants1.STAGE_FCA).first()
            FCrole = Group.objects.filter(name=Constants1.ROLE_FC).first() 


            if status == Constants1.HM_HOLD and HMUser is not None and HMHoldstage is not None and HMrole is not None:
                CandidateApprovalModel.objects.create(
                    Candidate=candidate1,
                    approverName=HMUser.username,
                    FirstName=HMUser.first_name,
                    LastName=HMUser.last_name,
                    Email=HMUser.email,
                    Stage=HMHoldstage,
                    role=HMrole,
                    approvalStatus='N',
                    approvalDate=None,
                    approvalComments=None,
                    CreatedOn=datetime.now())
            
            if status == Constants1.FURTHERREVIEW and HMUser is not None and HMFurtherReviewstage is not None and HMrole is not None:
                CandidateApprovalModel.objects.create(
                    Candidate=candidate1,
                    approverName=HMUser.username,
                    FirstName=HMUser.first_name,
                    LastName=HMUser.last_name,
                    Email=HMUser.email,
                    Stage=HMFurtherReviewstage,
                    role=HMrole,
                    approvalStatus='N',
                    approvalDate=None,
                    approvalComments=None,
                    CreatedOn=datetime.now())
            
            if status == Constants1.BH_CANDIDATE_APPROVAL and FCuser is not None and FCApprovalstage is not None and FCrole is not None:
                CandidateApprovalModel.objects.create(
                    Candidate=candidate1,
                    approverName=FCuser.username,
                    FirstName=FCuser.first_name,
                    LastName=FCuser.last_name,
                    Email=FCuser.email,
                    Stage=FCApprovalstage,
                    role=FCrole,
                    approvalStatus='N',
                    approvalDate=None,
                    approvalComments=None,
                    CreatedOn=datetime.now())
            
            if status == Constants1.BH_CANDIDATE_APPROVAL and GMuser is not None and GMApprovalstage is not None and GMrole is not None:
                CandidateApprovalModel.objects.create(
                    Candidate=candidate1,
                    approverName=GMuser.username,
                    FirstName=GMuser.first_name,
                    LastName=GMuser.last_name,
                    Email=GMuser.email,
                    Stage=GMApprovalstage,
                    role=GMrole,
                    approvalStatus='N',
                    approvalDate=None,
                    approvalComments=None,
                    CreatedOn=datetime.now())
            # if status == Constants1.BH_CANDIDATE_APPROVAL and GMuser is not None and GMApprovalstage is not None and GMrole is not None:
            #     CandidateApprovalModel.objects.create(
            #         Candidate=candidate1,
            #         approverName=GMuser.username,
            #         FirstName=GMuser.first_name,
            #         LastName=GMuser.last_name,
            #         Email=GMuser.email,
            #         Stage=GMApprovalstage,
            #         role=GMrole,
            #         approvalStatus='N',
            #         approvalDate=None,
            #         approvalComments=None,
            #         CreatedOn=datetime.now())
            if status == Constants1.HR_HOLD and HRuser is not None and HRHoldstage is not None and HRrole is not None:
                CandidateApprovalModel.objects.create(
                    Candidate=candidate1,
                    approverName=HRuser.username,
                    FirstName=HRuser.first_name,
                    LastName=HRuser.last_name,
                    Email=HRuser.email,
                    Stage=HRHoldstage,
                    role=HRrole,
                    approvalStatus='N',
                    approvalDate=None,
                    approvalComments=None,
                    CreatedOn=datetime.now())
            # if status == Constants1.HOLD_AT_HM_INTERVIEW and HMUser is not None and HMHoldstage is not None and HMrole is not None:
            #     CandidateApprovalModel.objects.create(
            #     Candidate = candidate1,
            #     approverName =  HMUser.username,
            #     FirstName = HMUser.first_name,
            #     LastName = HMUser.last_name,
            #     Email = HMUser.email,
            #     Stage = HRHoldstage,
            #     role = HMrole,
            #     approvalStatus = 'N',
            #     approvalDate = None,
            #     approvalComments = None,
            #     CreatedOn = datetime.now())
        except Exception as exp:
            success = False
            raise Exception(Messages1.ERR_SAVE_APP_DATA+str(exp))
        return success
    def addselectedcandidate(self,candidateob):
        print(candidateob)
        selectedcandidatesvar=Selected_Candidates
        # addselectedcandidatesserializer=AddSelectedCandidatesSerializer(data=candidateob)
       
        try:
            # res= addselectedcandidatesserializer.save(
            Selected_Candidates.objects.create(
                candidate=candidateob,
                IsOfferAccepted=False,
                IsJoined=False,
                HRCID=None,
                EmployeeID=None,
                designation=None,
                subband=None,#foerign key
                band=None,#foerign key
                DateOfJoining=None,
                FixedCTC=0,
                VariablePercentage=None,
                MQVariable="N",
                FinalCTC=0,
                candidatecategory=None,#foreign key
                Is_Eligible_annu_Mgnt_Bonus=False,
                Is_Eligible_Joining_Bonus=False,
                IS_Eligible_Monthly_Incentive=False,
                Created_By="",
                Created_on=datetime.now(),
                Modified_By=None,
                Modified_On=None,
            )
            
            # create({
            #     candidate=candidateob
            # })
            # if res==True:
            #     return
        except Exception as  e:
                return Response(str(e))

