from candidate.models.selected_Candidates_Model import Selected_Candidates
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from candidate.models.candidatemodel import Candidate
from candidate.models.selected_Candidates_Model import  Selected_Candidates
from jobpost.models.jobpostapprovalmodel import JobPostApproval
from candidate.serializers import selectedcandidatesgridviewSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from ManageBand.models import Band
from ManageSubBand.models import SubBand
from ManageDesignation.models import Designation
from datetime import datetime

class updateselectedcandidate(ModelViewSet):
    @action(detail=True, methods=['post'])
    def updateselcandidate(self, request, format=None):
        # print(request.data)
        # CandidateActionModel1 = CandidateActionModel.objects.filter(
        #     ApproverName=request.data["ApproverName"])
        # CandidateActionModel_serializer = CandidateActionModelSerializer(
        #     CandidateActionModel1, many=True)
        try:
            
            sco =  Selected_Candidates.objects.filter(Selected_Candidate_ID=request.data["selectedcandidateid"]).update(


                designation= Designation.objects.get(DesignationId=request.data['DesignationId']),
                band=Band.objects.get(BandId=request.data['BandId']),
                subband=SubBand.objects.get(SubBandId=request.data['SubBandId']),
                DateOfJoining=request.data["DateOfJoining"],
                FixedCTC=request.data["FixedCTC"],
                VariablePercentage=request.data["VariablePercentage"],
                MQVariable=request.data["MQVariable"],
                Is_Eligible_annu_Mgnt_Bonus=request.data["IS_Eligible_annu_Mgnt_Bonus"],
                Is_Eligible_Joining_Bonus=request.data["IS_Eligible_Joining_Bonus"],
                IS_Eligible_Monthly_Incentive=request.data["IS_Eligible_Monthly_Incentive"],
                Modified_By=request.data["Modified_By"],
                Modified_On=datetime.now()

            )
            return  Response("working1",status=status.HTTP_200_OK)
        except Exception as e:
            return  Response(e,status=status.HTTP_400_BAD_REQUEST)




        # return Response("working",status=status.HTTP_200_OK)
        #terinary operator  in python?