from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from candidate.models.candidateactionmodel import CandidateActionModel
from candidate.serializers import CandidateActionModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class CandidateAction(ModelViewSet):
    @action(detail=True, methods=['post'])
    def candidateactiondetails(self, request, format=None):     
        print(request.data)   
        CandidateActionModel1 = CandidateActionModel.objects.filter(ApproverName=request.data["ApproverName"])
        CandidateActionModel_serializer = CandidateActionModelSerializer(CandidateActionModel1, many=True)
        return Response(CandidateActionModel_serializer.data)