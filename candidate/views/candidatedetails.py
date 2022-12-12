
from rest_framework import status  
from rest_framework.response import Response
from rest_framework.views import APIView

from candidate.models.candidatemodel import Candidate
from candidate.serializers import CandidateDetailsGridSerializer
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
import base64

class CandidateDetails(ModelViewSet):
    @action(detail=True, methods=['post'])
    def candidatedetails(self, request, format=None): 

        candidates = Candidate.objects.filter(Jobpost_id=request.data["jobpostID"])
        CandidateDetailsGrid_serializer = CandidateDetailsGridSerializer(candidates, many=True)
        return Response(CandidateDetailsGrid_serializer.data)
    @action(detail=True, methods=['post'])
    def download(self,request):
        print(request.data["Resume"])
        file_path = os.path.join( request.data["Resume"])
        print(file_path)
        # file_path=file_path.replace("/", "\\")
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response=base64.b64encode(fh.read())
                # response = HttpResponse(fh.read(), content_type="application/pdf")
                # response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                # return response
                return HttpResponse(response, content_type="text/html")
        return Response("File not found", status=status.HTTP_404_NOT_FOUND)