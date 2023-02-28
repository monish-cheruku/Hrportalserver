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


class documentuploadview(ModelViewSet):
    @action(detail=True, methods=["post"])
    def createdocument(self, request, format=None):
        try:
            

            documentuploadserializer = Documentuploadserializer(
                data=request.data, context=request.FILES)
            if documentuploadserializer.is_valid():
               
                duo = documentuploadserializer.save()

            return Response("success", status=status.HTTP_200_OK)
            
        except Exception as exp:
            # exp.with_traceback()
            return Response(exp, status=status.HTTP_400_BAD_REQUEST)

    
    def getotherdocuments(self,request,format=None):
        try:
            alldocsobj=CandidateDocumentsUpload.objects.filter(selectedcandidate_id=request.data["selectedcandidateid"],detailtypeId=0)
            serializeddata=CandidatedocumentsSerializer(alldocsobj,many=True).data
            return  Response(serializeddata,status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)
    def downloaddetaildocuments(self, request, format=None):
        try:
            file = request.data["file"]

            filename = os.path.join(BASE_DIR, str(file))
            filename = filename.replace("/", "\\")
            print(filename)
            if os.path.exists(filename):
                with open(filename, 'rb') as fh:
                    response = base64.b64encode(fh.read())
                    return HttpResponse(response, content_type="text/html")
            else:
                return Response("File path doesnt exist", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def deletedocument(self, request, format=None):

        try:
            do = CandidateDocumentsUpload.objects.filter(
                id=request.data["fileid"]).first()
            filename = do.file
            filename = os.path.join(MEDIA_ROOT, str(filename))
            filename = filename.replace("/", "\\")
            if os.path.exists(filename):
                os.remove(filename)
                do = CandidateDocumentsUpload.objects.filter(
                    id=request.data["fileid"]).first()
                do.delete()
            else:
                print("no file exist")

            return Response("deleted Sucessfully", status=status.HTTP_200_OK)
        except Exception as e:
            return Response("File path doesnt exist", status=status.HTTP_400_BAD_REQUEST)
