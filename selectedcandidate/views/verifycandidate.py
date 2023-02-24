import base64
import os
from smtplib import SMTPResponseException
from candidate.models.selected_Candidates_Model import Selected_Candidates
from rest_framework.response import Response
from rest_framework import status
from candidate.models.selected_Candidates_Model import Selected_Candidates
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from selectedcandidate.models.Candidatedducationaldetails import CandidateEducationalDetails
from selectedcandidate.models.Documentsupload import CandidateDocumentsUpload
from selectedcandidate.models import *
from candidate.models.selected_Candidates_Model import Selected_Candidates
from HRproj.settings import MEDIA_ROOT, MEDIA_URL, BASE_DIR
from django.http import HttpResponse, Http404

class Verifycandidate(ModelViewSet):
    @action(detail=True,methods=["post"])
    def Verifycandidate(self,request,format=None):
        try:
            SelectedCandidateob=Selected_Candidates.objects.get(Selected_Candidate_ID=request.data["selectedcandidateid"])
            if request.data["Verificationstatus"]=="completed":
                
                SelectedCandidateob.VerificationStatus=request.data["Verificationstatus"]
                SelectedCandidateob.save()
                return Response("Candidate verified", status=status.HTTP_200_OK)
            else:
                
                SelectedCandidateob.VerificationStatus=request.data["Verificationstatus"]
                SelectedCandidateob.VerificationComments=request.data["VerificationComments"]
                SelectedCandidateob.save()

                return Response("Notified candidate to change files", status=status.HTTP_200_OK)



        except Exception as e:
            return Response("failed to verify candidate ", status=status.HTTP_400_BAD_REQUEST)