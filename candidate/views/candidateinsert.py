from django.shortcuts import render
from rest_framework.views import APIView
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from candidate.models.candidateapprovalmodel import CandidateApprovalModel
from candidate.models.candidatemodel import Candidate  
from datetime import datetime
from candidate.serializers import CandidatePostSerializer, CandidatePutSerializer
from django.contrib.auth.models import User, Group
from jobpost.models.jobpostapprovalmodel import JobPostApproval
from jobpost.models.jobpostuserrolesmodel import JobPostUserRolesModel
from managestages.models import Stage
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1

class CandidateApi(APIView):

    
    def post(self, request, format=None):        
        try:
            with transaction.atomic():
                CandidatePost_serializer = CandidatePostSerializer(data=request.data)    
                if CandidatePost_serializer.is_valid():
                    candidate1 = CandidatePost_serializer.save()
                    if candidate1 is not None:                             
                        success = self.insertorupdatecandidateapproval(candidate1, request.data)
                        if success == True:
                    # return Response({"status": "success", "data": company_serializer.data}, status=status.HTTP_200_OK)  
                            return Response(Messages1.CAN_PRF_CRTD_SCFL, status=status.HTTP_200_OK)
                        else:
                            return Response(Messages1.Can_PRF_CRTN_FAIL, status=status.HTTP_400_BAD_REQUEST)                     
                    
                return Response(CandidatePost_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        except Exception as exp:
            # exp.with_traceback()
            return Response(Messages1.ERR_CRTG_PRF+str(exp), status=status.HTTP_400_BAD_REQUEST)
        # return Response("Exception while creation Job Post", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):         
        candidate =  Candidate.objects.get(CandidateId=request.data['CandidateId'])
        # jobpost.ModifiedBy = ""
        candidate.ModifiedOn = datetime.now()
        if(type(request.data["Resume"]) is str):
            print("old file name")
            CandidatePost_serializer = CandidatePutSerializer(candidate ,data=request.data)
        else:
            print("new file ") 
            CandidatePost_serializer = CandidatePostSerializer(candidate ,data=request.data)
        if CandidatePost_serializer.is_valid():
            candidate1 = CandidatePost_serializer.save()
            if candidate1 is not None:
                self.insertorupdatecandidateapproval(candidate1, request.data)
                return Response(Messages1.UPD_SCFL)
        return Response(CandidatePost_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST) 


    def insertorupdatecandidateapproval(self, candidate1, data):
        success = True
        try:
            # Hiring Manager
            HMUserName =  candidate1.Jobpost.UserName
            # HR
            # HRstage = Stage.objects.filter(StageName=Constants1.Stage_PP).first()
            # HR1role = Group.objects.filter(name=Constants1.Role_HR).first()  
            # jobpostHRApprover = JobPostApproval.objects.filter(jobpost= candidate1.Jobpost, Stage =HRstage, role=HR1role).first()
            # if jobpostHRApprover is not None:
            #     HRUserName = jobpostHRApprover.approverName
            # else:
            #     HRUserName = ""      
            # Finannce Controller
            HRUserObj =  JobPostUserRolesModel.objects.filter(RoleName = Constants1.ROLE_HR).first()
            if HRUserObj is not None:
                HRUserName = HRUserObj.UserName
            else:
                HRUserName = ""      
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
           
            print("HMUserName Name --"+HMUserName)
            print("HRUserName Name --"+HRUserName)
            print("FCUserName Name --"+FCUserName)
            print("GMUserName Name --"+GMUserName)

            HMUser = User.objects.get(username=HMUserName)
            HMCandReviewstage = Stage.objects.filter(StageName=Constants1.STAGE_CR).first()
            HMCandInterviewstage = Stage.objects.filter(StageName=Constants1.STAGE_CI).first()
            HMrole = Group.objects.filter(name=Constants1.ROLE_HM).first()

            HRuser = User.objects.get(username=HRUserName)
            HRInterviewstage = Stage.objects.filter(StageName=Constants1.STAGE_HR_INTERVIEW).first()
            HRrole = Group.objects.filter(name=Constants1.ROLE_HR).first()

            # GMuser = User.objects.get(username=GMUserName)
            # GMApprovalstage = Stage.objects.filter(StageName=Constants1.STAGE_GMA).first()
            # GMrole = Group.objects.filter(name=Constants1.ROLE_GM).first() 

            # FCuser = User.objects.get(username=FCUserName)
            # FCApprovalstage = Stage.objects.filter(StageName=Constants1.STAGE_FCA).first()
            # FCrole = Group.objects.filter(name=Constants1.ROLE_FC).first() 
            #     
            
            BHrole = Group.objects.filter(name=Constants1.ROLE_BH).first()
            BHstage = Stage.objects.filter(StageName=Constants1.STAGE_BHA).first()
            jobpostapprovalBH = JobPostApproval.objects.filter(jobpost= candidate1.Jobpost, Stage=BHstage, role=BHrole).first()
            BHName=jobpostapprovalBH.approverName

            BHUser = User.objects.get(username=BHName)
            BHCandidateApprovalStage = Stage.objects.filter(StageName=Constants1.STAGE_BH_CANDIDATE_APPROVAL).first()


            if (HMUser is not None and HMCandReviewstage is not None and HMrole is not None):
                candidatereviewHM = CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=HMCandReviewstage, role=HMrole).first()
                if candidatereviewHM is not None:
                    CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=HMCandReviewstage, role=HMrole).update(
                    # jobPostApprovalId = jobpostapprovalBH.jobPostApprovalId,    
                    Candidate = candidate1,
                    approverName =  HMUser.username,
                    FirstName = HMUser.first_name,
                    LastName = HMUser.last_name,
                    Email = HMUser.email,
                    Stage = HMCandReviewstage,
                    role = HMrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
                else:
                    CandidateApprovalModel.objects.create(
                    Candidate = candidate1,
                    approverName =  HMUser.username,
                    FirstName = HMUser.first_name,
                    LastName = HMUser.last_name,
                    Email = HMUser.email,
                    Stage = HMCandReviewstage,
                    role = HMrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())   


            if (HMUser is not None and HMCandInterviewstage is not None and HMrole is not None):
                candidateinterviewHM = CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=HMCandInterviewstage, role=HMrole).first()
                if candidateinterviewHM is not None:
                    CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=HMCandInterviewstage, role=HMrole).update(
                    # jobPostApprovalId = jobpostapprovalBH.jobPostApprovalId,    
                    Candidate = candidate1,
                    approverName =  HMUser.username,
                    FirstName = HMUser.first_name,
                    LastName = HMUser.last_name,
                    Email = HMUser.email,
                    Stage = HMCandInterviewstage,
                    role = HMrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
                else:
                    CandidateApprovalModel.objects.create(
                    Candidate = candidate1,
                    approverName =  HMUser.username,
                    FirstName = HMUser.first_name,
                    LastName = HMUser.last_name,
                    Email = HMUser.email,
                    Stage = HMCandInterviewstage,
                    role = HMrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())       


            if (HRuser is not None and HRInterviewstage is not None and HRrole is not None):
                candidateinterviewHR = CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=HRInterviewstage, role=HRrole).first()
                if candidateinterviewHR is not None:
                    CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=HRInterviewstage, role=HRrole).update(              
                    Candidate = candidate1,
                    approverName =  HRuser.username,
                    FirstName = HRuser.first_name,
                    LastName = HRuser.last_name,
                    Email = HRuser.email,
                    Stage = HRInterviewstage,
                    role = HRrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
                else:
                    CandidateApprovalModel.objects.create(
                    Candidate = candidate1,
                    approverName =  HRuser.username,
                    FirstName = HRuser.first_name,
                    LastName = HRuser.last_name,
                    Email = HRuser.email,
                    Stage = HRInterviewstage,
                    role = HRrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
            # if (GMuser is not None and GMApprovalstage is not None and GMrole is not None):
            #     candidateapprovalGM = CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=GMApprovalstage, role=GMrole).first()
            #     if candidateapprovalGM is not None:
            #         CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=GMApprovalstage, role=GMrole).update(              
            #         Candidate = candidate1,
            #         approverName =  GMuser.username,
            #         FirstName = GMuser.first_name,
            #         LastName = GMuser.last_name,
            #         Email = GMuser.email,
            #         Stage = GMApprovalstage,
            #         role = GMrole,
            #         approvalStatus = Constants1.NA,
            #         approvalDate = None,
            #         approvalComments = None,
            #         CreatedOn = datetime.now())
            #     else:
            #         CandidateApprovalModel.objects.create(
            #         Candidate = candidate1,
            #         approverName =  GMuser.username,
            #         FirstName = GMuser.first_name,
            #         LastName = GMuser.last_name,
            #         Email = GMuser.email,
            #         Stage = GMApprovalstage,
            #         role = GMrole,
            #         approvalStatus = Constants1.NA,
            #         approvalDate = None,
            #         approvalComments = None,
            #         CreatedOn = datetime.now())
            # if (FCuser is not None and FCApprovalstage is not None and FCrole is not None):
            #     candidateapprovalFC = CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=FCApprovalstage, role=FCrole).first()
            #     if candidateapprovalGM is not None:
            #         CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=FCApprovalstage, role=FCrole).update(              
            #         Candidate = candidate1,
            #         approverName =  FCuser.username,
            #         FirstName = FCuser.first_name,
            #         LastName = FCuser.last_name,
            #         Email = FCuser.email,
            #         Stage = FCApprovalstage,
            #         role = FCrole,
            #         approvalStatus = Constants1.NA,
            #         approvalDate = None,
            #         approvalComments = None,
            #         CreatedOn = datetime.now())
            #     else:
            #         CandidateApprovalModel.objects.create(
            #         Candidate = candidate1,
            #         approverName =  FCuser.username,
            #         FirstName = FCuser.first_name,
            #         LastName = FCuser.last_name,
            #         Email = FCuser.email,
            #         Stage = FCApprovalstage,
            #         role = FCrole,
            #         approvalStatus = Constants1.NA,
            #         approvalDate = None,
            #         approvalComments = None,
            #         CreatedOn = datetime.now())        
            if (BHUser is not None and BHCandidateApprovalStage is not None and BHrole is not None):
                CandidateApprovalBH = CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=BHCandidateApprovalStage, role=BHrole).first()
                if CandidateApprovalBH is not None:
                    CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=BHCandidateApprovalStage, role=BHrole).update(              
                    Candidate = candidate1,
                    approverName =  BHUser.username,
                    FirstName = BHUser.first_name,
                    LastName = BHUser.last_name,
                    Email = BHUser.email,
                    Stage = BHCandidateApprovalStage,
                    role =BHrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
                else:
                    CandidateApprovalModel.objects.create(
                    Candidate = candidate1,
                    approverName =  BHUser.username,
                    FirstName = BHUser.first_name,
                    LastName = BHUser.last_name,
                    Email = BHUser.email,
                    Stage = BHCandidateApprovalStage,
                    role =BHrole,
                    approvalStatus = Constants1.NA,
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())                    
        except Exception as exp:
            success = False
            raise Exception (Messages1.ERR_SAVE_APP_DATA+str(exp))
        return success            