from django.db import models
from rest_framework.viewsets import ModelViewSet
import os
from candidate.models.selected_Candidates_Model import Selected_Candidates
from rest_framework.response import Response
from rest_framework import status

class Acceptofferletter(ModelViewSet):
 def acceptofferletter(self,request,format=None):
        try:
            Selected_Candidates.objects.filter(Selected_Candidate_ID=request.data["selectedcandidateid"]).update(IsOfferAccepted=True)

            # selcanobj=Selected_Candidates.objects.filter(Selected_Candidate_ID=request.data["selectedcandidateid"]).first()
            # if selcanobj is not None:
            #     selcanobj.update(
            #         IsOfferAccepted=True
            #     )
            return  Response("Offer Letter Accepted",status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)