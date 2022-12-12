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
                            return Response("Candidate profile Created Successfully", status=status.HTTP_200_OK)
                        else:
                            return Response("Candidate profile Creation failed", status=status.HTTP_400_BAD_REQUEST)                     
                    
                return Response(CandidatePost_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        except Exception as exp:
            # exp.with_traceback()
            return Response("Exception while profile creation "+str(exp), status=status.HTTP_400_BAD_REQUEST)
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
                return Response("Updated Successfully")
        return Response(CandidatePost_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    def insertorupdatecandidateapproval(self, candidate1, data):
        success = True
        try:
            # Hiring Manager
            HMUserName =  candidate1.Jobpost.UserName
            # HR
            HRstage = Stage.objects.filter(StageName="Profiles Pending").first()
            HR1role = Group.objects.filter(name="HR").first()  
            jobpostHRApprover = JobPostApproval.objects.filter(jobpost= candidate1.Jobpost, Stage =HRstage, role=HR1role).first()
            if jobpostHRApprover is not None:
                HRUserName = jobpostHRApprover.approverName
            else:
                HRUserName = ""      
            # Finannce Controller
            FCUserObj =  JobPostUserRolesModel.objects.filter(RoleName = "Finance Controller").first()
            if FCUserObj is not None:
                FCUserName = FCUserObj.UserName
            else:
                FCUserName = ""  
            # General Manager
            GMUserObj =  JobPostUserRolesModel.objects.filter(RoleName = "General Manager").first()
            if GMUserObj is not None:
                GMUserName = GMUserObj.UserName
            else:
                GMUserName = ""  
           
            print("HMUserName Name --"+HMUserName)
            print("HRUserName Name --"+HRUserName)
            print("FCUserName Name --"+FCUserName)
            print("GMUserName Name --"+GMUserName)

            HMUser = User.objects.get(username=HMUserName)
            HMCandReviewstage = Stage.objects.filter(StageName="Candidate Review").first()
            HMCandInterviewstage = Stage.objects.filter(StageName="Candidate Interview").first()
            HMrole = Group.objects.filter(name="Hiring Manager").first()

            HRuser = User.objects.get(username=HRUserName)
            HRInterviewstage = Stage.objects.filter(StageName="Shortlisted").first()
            HRrole = Group.objects.filter(name="HR").first()

            GMuser = User.objects.get(username=GMUserName)
            GMApprovalstage = Stage.objects.filter(StageName="GM Approval").first()
            GMrole = Group.objects.filter(name="General Manager").first() 

            FCuser = User.objects.get(username=FCUserName)
            FCApprovalstage = Stage.objects.filter(StageName="FC Approval").first()
            FCrole = Group.objects.filter(name="Finance Controller").first()                          

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
                    approvalStatus = 'N',
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
                    approvalStatus = 'N',
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
                    approvalStatus = 'N',
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
                    approvalStatus = 'N',
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
                    approvalStatus = 'N',
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
                    approvalStatus = 'N',
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
            if (GMuser is not None and GMApprovalstage is not None and GMrole is not None):
                candidateapprovalGM = CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=GMApprovalstage, role=GMrole).first()
                if candidateapprovalGM is not None:
                    CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=GMApprovalstage, role=GMrole).update(              
                    Candidate = candidate1,
                    approverName =  GMuser.username,
                    FirstName = GMuser.first_name,
                    LastName = GMuser.last_name,
                    Email = GMuser.email,
                    Stage = GMApprovalstage,
                    role = GMrole,
                    approvalStatus = 'N',
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
                else:
                    CandidateApprovalModel.objects.create(
                    Candidate = candidate1,
                    approverName =  GMuser.username,
                    FirstName = GMuser.first_name,
                    LastName = GMuser.last_name,
                    Email = GMuser.email,
                    Stage = GMApprovalstage,
                    role = GMrole,
                    approvalStatus = 'N',
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
            if (FCuser is not None and FCApprovalstage is not None and FCrole is not None):
                candidateapprovalFC = CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=FCApprovalstage, role=FCrole).first()
                if candidateapprovalGM is not None:
                    CandidateApprovalModel.objects.filter(Candidate= candidate1, Stage=FCApprovalstage, role=FCrole).update(              
                    Candidate = candidate1,
                    approverName =  FCuser.username,
                    FirstName = FCuser.first_name,
                    LastName = FCuser.last_name,
                    Email = FCuser.email,
                    Stage = FCApprovalstage,
                    role = FCrole,
                    approvalStatus = 'N',
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())
                else:
                    CandidateApprovalModel.objects.create(
                    Candidate = candidate1,
                    approverName =  FCuser.username,
                    FirstName = FCuser.first_name,
                    LastName = FCuser.last_name,
                    Email = FCuser.email,
                    Stage = FCApprovalstage,
                    role = FCrole,
                    approvalStatus = 'N',
                    approvalDate = None,
                    approvalComments = None,
                    CreatedOn = datetime.now())                                          
        except Exception as exp:
            success = False
            raise Exception ("Error while saving approvers data"+str(exp))
        return success            