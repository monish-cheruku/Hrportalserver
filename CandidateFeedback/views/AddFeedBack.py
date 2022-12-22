from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from CandidateFeedback.serializers.AddFeedBackSerializer import AddFeedBackSerializer
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1
from candidate.models.candidateapprovalmodel import CandidateApprovalModel
from candidate.models.candidatemodel import Candidate
from django.db import transaction
import django_filters
from datetime import datetime
from django.contrib.auth.models import User, Group
from jobpost.models.jobpostuserrolesmodel import JobPostUserRolesModel

from managestages.models import Stage

# class AddFeedBack(APIView):
#     def post(self,request,format=None):
#         try:
#             print("working")
#             print(request.data)
#             res={"data":"working"}
#             return Response(res.data)
#         except:
#             return Response("failed",status=status.HTTP_400_BAD_REQUEST)

class AddFeedBack(generics.ListCreateAPIView):  
    # serializer_class = AddFeedBackSerializer 

    # def get_serializer(self, *args, **kwargs):  
    #     if isinstance(kwargs.get("data", {}), list):  
    #         kwargs["many"] = True  

    #     return super(AddFeedBack, self).get_serializer(*args, **kwargs) 


    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                candidateapprovalid=request.data.get("candidateapprovalid")
                candidateid=request.data.get("candidateid")
                Status=request.data.get("status")
                comments=request.data.get("comments")
                response = ''

                candidateob=Candidate.objects.filter(CandidateId=candidateid).first()
                ca=CandidateApprovalModel.objects.filter(CandidateApprovalId=candidateapprovalid).update(
                approvalStatus=Status,
                approvalDate=datetime.now(),
                approvalComments=comments 
                )
                # print(ca)
                # q = django_filters.Filter(method='my_custom_filter', label="Search")
                # print(q)
                if ca is not None:
                        
                    if (Status == Constants1.HM_SHORTLISTED):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_HR_INTERVIEW).first()
                        response="Candidate has been shortlisted for HR interview "
                    elif (Status == Constants1.HR_SHORTLISTED):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_BH_CANDIDATE_APPROVAL).first()
                        response="Candidate has been selected"

                    elif (Status == Constants1.HM_HOLD):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_HM_HOLD).first()
                        success=self.insertnewrow(candidateob,Status)
                        if success ==False:
                            raise Exception("error while creating new row in candidate approval table")
                        else:
                            response = "Candidate has been put on hold"
                   
                    elif (Status == Constants1.REJECTED):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_REJECTED).first()
                        response="Candidate has been rejected"
                    elif (Status == Constants1.FURTHERREVIEW):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_FURTHERREVIEW).first()
                        success=self.insertnewrow(candidateob,Status)
                        if success== False:
                            raise Exception("error while creating new row in candidate approval table")
                        else:
                            response = "Candidate has been shortlisted for further review"
                    candidatecount= Candidate.objects.filter(CandidateId=candidateid).update(
                        Stage =  stage
                       
                    )
                    
                    
               
                else:
                    raise Exception
                

                

                
                print("create bulk insert")
                print(request.data)
                serializer = AddFeedBackSerializer(data=request.data.get("feedback"),many=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(response,status=status.HTTP_200_OK)
        except Exception as exp:
            return Response(Messages1.ERR_FBK_CAN+str(exp), status=status.HTTP_400_BAD_REQUEST) 
    def insertnewrow(self,candidate1, status):
        success=True
        try:
            HMUserName =  candidate1.Jobpost.UserName
            HRUserName=""

            HRUserObj =  JobPostUserRolesModel.objects.filter(RoleName = Constants1.ROLE_HR).first()
            if HRUserObj is not None:
                HRUserName = HRUserObj.UserName
            else:
                HRUserName = "" 

            HRuser = User.objects.get(username=HRUserName)
            HRHoldstage = Stage.objects.filter(StageName=Constants1.STAGE_HR_HOLD).first()
            HRrole = Group.objects.filter(name=Constants1.ROLE_HR).first()

            HMUser = User.objects.get(username=HMUserName)

            HMHoldstage = Stage.objects.filter(StageName=Constants1.STAGE_HM_HOLD).first()
            HMFurtherReviewstage = Stage.objects.filter(StageName=Constants1.STAGE_FURTHERREVIEW).first()
            HMrole = Group.objects.filter(name=Constants1.ROLE_HM).first()

            if status == Constants1.HM_HOLD and HMUser is not None and HMHoldstage is not None and HMrole is not None:

                CandidateApprovalModel.objects.create(
                Candidate = candidate1,
                approverName =  HMUser.username,
                FirstName = HMUser.first_name,
                LastName = HMUser.last_name,
                Email = HMUser.email,
                Stage = HMHoldstage,
                role = HMrole,
                approvalStatus = 'N',
                approvalDate = None,
                approvalComments = None,
                CreatedOn = datetime.now())
            if status == Constants1.FURTHERREVIEW and HMUser is not None and HMFurtherReviewstage is not None and HMrole is not None:

                CandidateApprovalModel.objects.create(
                Candidate = candidate1,
                approverName =  HMUser.username,
                FirstName = HMUser.first_name,
                LastName = HMUser.last_name,
                Email = HMUser.email,
                Stage = HMFurtherReviewstage,
                role = HMrole,
                approvalStatus = 'N',
                approvalDate = None,
                approvalComments = None,
                CreatedOn = datetime.now())
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
            raise Exception (Messages1.ERR_SAVE_APP_DATA+str(exp))
        return success  