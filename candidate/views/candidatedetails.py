from rest_framework import status  
from rest_framework.response import Response
from rest_framework.views import APIView

from candidate.models.candidatemodel import Candidate
from candidate.serializers import CandidateDetailsGridSerializer

class CandidateDetails(APIView):

    def post(self, request, format=None): 

        candidates = Candidate.objects.filter(Jobpost_id=request.data["jobpostID"])
        CandidateDetailsGrid_serializer = CandidateDetailsGridSerializer(candidates, many=True)
        return Response(CandidateDetailsGrid_serializer.data)