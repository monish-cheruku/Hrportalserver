from rest_framework import serializers
from datetime import datetime
from HRproj.settings import MEDIA_ROOT, MEDIA_URL
from candidate.models.Candidate_Feedback_Model import Candidate_Feedback
from candidate.models.Feedback_Category_Model import Feedback_Category
from candidate.models.candidateapprovalmodel import CandidateApprovalModel
from candidate.models.candidatemodel import Candidate
from jobpost.models.jobpostmodel import JobPost
from managestages.models import Stage
from candidate.models.candidateactionmodel import CandidateActionModel
import os
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1
from candidate.models.selected_Candidates_Model import Selected_Candidates
from jobpost.serializers import JobPostDetailsGridSerializer
from selectedcandidate.models.CandidatePersonalInfo import CandidatePersonalInfo
from selectedcandidate.models.CandidateFamilyDetails import CandidateFamilyDetails
from selectedcandidate.models.CandidateEducationalDetails import CandidateEducationalDetails
from selectedcandidate.models.CandidateEmployentDetails import CandidateEmployementDetials




class candidatepersonalinfogetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatePersonalInfo
        fields="__all__"


class candidatefamilydetailgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateFamilyDetails
        fields="__all__"
class candidateeducationdetailgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateEducationalDetails
        fields="__all__"
class candidateemployementdetailgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateEmployementDetials
        fields="__all__"