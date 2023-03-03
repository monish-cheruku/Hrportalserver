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
from selectedcandidate.Serializers import Documentuploadserializer
from selectedcandidate.Serializers import CandidatedocumentsSerializer
from selectedcandidate.models import *
from candidate.models.selected_Candidates_Model import Selected_Candidates
from HRproj.settings import MEDIA_ROOT, MEDIA_URL, BASE_DIR
from django.http import HttpResponse, Http404

class Verifydocument(ModelViewSet):
 def Verifydocument(self,request,format=None):
    try:
        # do = CandidateDocumentsUpload.objects.filter(
        #     id=request.data["fileid"]).update(verified=request.data["verified"])
        candidatedocob= CandidateDocumentsUpload.objects.get(id=request.data["fileid"])
        selcanid=candidatedocob.selectedcandidate_id
        if request.data["verified"]=='verified':
            candidatedocob.verified="verified"
            candidatedocob.verificationcomments=""
            candidatedocob.save()
        else:
            candidatedocob.verified="rejected"
            candidatedocob.verificationcomments=request.data["verificationcomments"]
            candidatedocob.save()

        #check all other documents for candidate and update verification status in selected candidate table
        # alldocs=CandidateDocumentsUpload.objects.filter(selectedcandidate=selcanid)
        # for i in alldocs:
        #     i.se


        
        #prev pending curent verified status trigger mail

        return Response("document verification updated", status=status.HTTP_200_OK)
    except Exception as e:
        return Response("failed to verify document ", status=status.HTTP_400_BAD_REQUEST)