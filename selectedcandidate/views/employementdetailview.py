from candidate.models.selected_Candidates_Model import Selected_Candidates
from rest_framework.response import Response
from rest_framework import status
from candidate.models.selected_Candidates_Model import  Selected_Candidates
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from selectedcandidate.models import CandidateEmployentDetails
from selectedcandidate.Serializers import candidateemployementdetailgetSerializer
from selectedcandidate.models import *
from candidate.models.selected_Candidates_Model import Selected_Candidates


class employementdetailsview(ModelViewSet):
    @action(detail=True,methods=["post"])
    def createemployementdetail(self,request,format=None):
        try:
            # CandidatePersonalInfo.objects.all()
            CandidateEmployentDetails.CandidateEmployementDetials .objects.create(
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

            CandidateEmployentDetails.CandidateEmployementDetials.objects.filter(id=request.data["id"]).update(
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

            empdo=CandidateEmployentDetails.CandidateEmployementDetials.objects.filter(selectedCandidateId_id=request.data["selectedcandidateid"])
            empdos=candidateemployementdetailgetSerializer(empdo,many=True).data
            return  Response(empdos,status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)
    def deleteemployementdetail(self,request,format=None):
        try:

            empdo=CandidateEmployentDetails.CandidateEmployementDetials.objects.filter(id=request.data["id"]).first()
            empdo.delete()
            return  Response("deleted Sucessfully",status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)