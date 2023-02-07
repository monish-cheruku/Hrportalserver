from candidate.models.selected_Candidates_Model import Selected_Candidates
from rest_framework.response import Response
from rest_framework import status
from candidate.models.selected_Candidates_Model import  Selected_Candidates
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from selectedcandidate.models.Candidateemployementdetails import CandidateEmployementDetials
from selectedcandidate.models.Documentsupload import CandidateDocumentsUpload
from selectedcandidate.Serializers import candidateemployementdetailgetSerializer
from selectedcandidate.models import *
from candidate.models.selected_Candidates_Model import Selected_Candidates
import os
from django.db import transaction
from HRproj.settings import MEDIA_ROOT, MEDIA_URL, BASE_DIR

class employementdetailsview(ModelViewSet):
    @action(detail=True,methods=["post"])
    def createemployementdetail(self,request,format=None):
        try:
            # CandidatePersonalInfo.objects.all()
            CandidateEmployementDetials.objects.create(
            selectedCandidateId=Selected_Candidates.objects.filter(Selected_Candidate_ID=request.data["selectedcandidateid"]).first(),
      PreviousCompanyName=request.data["PreviousCompanyName"],
        PreviousCompanyAddress=request.data["PreviousCompanyAddress"],
        Start_Date=request.data["Start_Date"],
        End_Date=request.data["End_Date"],
        Designationonjoining=request.data["Designationonjoining"],
        Designationonleaving=request.data["Designationonleaving"],
            





            )
            return  Response("employement detail created",status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return  Response(e,status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True,methods=["post"])
    def updateemployementdetails(self,request,format=None):
        try:

            CandidateEmployementDetials.objects.filter(id=request.data["id"]).update(
                 selectedCandidateId=Selected_Candidates.objects.filter(Selected_Candidate_ID=request.data["selectedcandidateid"]).first(),
      PreviousCompanyName=request.data["PreviousCompanyName"],
        PreviousCompanyAddress=request.data["PreviousCompanyAddress"],
        Start_Date=request.data["Start_Date"],
        End_Date=request.data["End_Date"],
        Designationonjoining=request.data["Designationonjoining"],
        Designationonleaving=request.data["Designationonleaving"],
            





            )
            return  Response("employement details updated ",status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True,methods=["post"])
    def getemployementdetails(self,request,format=None):
        try:

            empdo=CandidateEmployementDetials.objects.filter(selectedCandidateId_id=request.data["selectedcandidateid"])
            empdos=candidateemployementdetailgetSerializer(empdo,many=True).data
            return  Response(empdos,status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)
    def deleteemployementdetail(self,request,format=None):
        try:
            with transaction.atomic():
                empdo=CandidateEmployementDetials.objects.filter(id=request.data["id"]).first()
                empdo.delete()
                candidatedocob=CandidateDocumentsUpload.objects.filter(detailtype="Employment",detailtypeId=request.data["id"])

                for i in candidatedocob:
                
                    filename =i.file
                    filename = os.path.join(MEDIA_ROOT, str(filename))
                    filename = filename.replace("/", "\\")
                    if os.path.exists(filename):
                        os.remove(filename)
                    
                    else:
                        print("no file exist")





                candidatedocob.delete()



                return  Response("deleted Sucessfully",status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)