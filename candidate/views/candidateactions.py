from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from candidate.models.candidateactionmodel import CandidateActionModel
from candidate.serializers import CandidateActionModelSerializer
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


class CandidateAction(ModelViewSet):
    @action(detail=True, methods=['post'])
    def candidateactiondetails(self, request, format=None):     
        print(request.data)   
        CandidateActionModel1 = CandidateActionModel.objects.filter(ApproverName=request.data["ApproverName"])
        CandidateActionModel_serializer = CandidateActionModelSerializer(CandidateActionModel1, many=True)
        return Response(CandidateActionModel_serializer.data)

    @action(detail=True, methods=['post'])
    def candidatereviewsubmit(self, request, format=None): 
        candidateApprovalId =  request.data['CandidateApprovalId']
        candidateId =  request.data['CandidateId']
        reviewStatus =  request.data['reviewStatus']
        reviewComments =  request.data['reviewComments']
        response = ''
        
        try:
            with transaction.atomic():
                candidateReview =  CandidateApprovalModel.objects.filter(CandidateApprovalId=candidateApprovalId).update(
                    approvalDate = datetime.now(),
                    approvalStatus = reviewStatus,
                    approvalComments = reviewComments,
                )
                
                if candidateReview is not None:
                    if (reviewStatus == Constants1.STAGE_CI):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_CI).first()
                        response = Messages1.CAN_IP
                    elif (reviewStatus == Constants1.STAGE_CANR):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_CANR).first()
                        response = Messages1.CAN_RJCTD
                    print(stage.StageId)
                    candidates =  Candidate.objects.filter(CandidateId=candidateId).update(
                        Stage =  stage   
                    )
                    print(candidates)
                    return Response(response, status=status.HTTP_200_OK) 
                
        except Exception as exp:
            return Response(Messages1.ERR_APP_CAN_DTLS+str(exp), status=status.HTTP_400_BAD_REQUEST)      
