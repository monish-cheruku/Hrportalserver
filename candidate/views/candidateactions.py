from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from candidate.models.candidateactionmodel import CandidateActionModel
from candidate.serializers import AddFeedBackSerializer, CandidateActionModelSerializer
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


class CandidateAction(ModelViewSet):
    @action(detail=True, methods=['post'])
    def candidateactiondetails(self, request, format=None):     
        print(request.data)   
        CandidateActionModel1 = CandidateActionModel.objects.filter(ApproverName=request.data["ApproverName"])
        CandidateActionModel_serializer = CandidateActionModelSerializer(CandidateActionModel1, many=True)
        return Response(CandidateActionModel_serializer.data)

    @action(detail=True, methods=['post'])
    def candidateworkflowsubmit(self, request, format=None): 
        try:
            with transaction.atomic():
                candidateapprovalid=request.data["candidateapprovalid"]
                candidateid=request.data["candidateid"]
                Status=request.data["status"]
                comments=request.data["comments"]
                feedback = request.data["feedback"]

                response = ''

                candidateob=Candidate.objects.filter(CandidateId=candidateid).first()
                ca=CandidateApprovalModel.objects.filter(CandidateApprovalId=candidateapprovalid).update(
                approvalStatus=Status,
                approvalDate=datetime.now(),
                approvalComments=comments 
                )

                if ca is not None:
                    if (Status == Constants1.SELECT_FOR_INTERVIEW):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_CI).first()
                        response = Messages1.CAN_IP    
                    elif (Status == Constants1.HM_SHORTLISTED):
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

                if feedback is not None:
                    print("create bulk insert")
                    print(request.data)
                    serializer = AddFeedBackSerializer(data=feedback,many=True)
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