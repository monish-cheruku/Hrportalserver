from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from candidate.models.selected_Candidates_Model import Selected_Candidates
from candidate.serializers import selectedcandidatesgridviewSerializer
# from selectedcandidate.models.CandidatePersonalInfo import *
from selectedcandidate.models.CandidatePersonalInfo import * 
from selectedcandidate.models.CandidateEducationalDetails import * 
from selectedcandidate.models.CandidateEmployentDetails import * 
from selectedcandidate.models.CandidateFamilyDetails import * 
from selectedcandidate.models.CandidateInsuranceDetails import * 
from selectedcandidate.models.Documentsupload import * 



class SelectedCandidateAction(ModelViewSet):
    @action(detail=True, methods=['post'])
    def selectedcandidatedetailsbyemail(self, request, format=None):
        try:
            # CandidatePersonalInfo.objects.all()
            print(request.data)
            selectedcandidate = Selected_Candidates.objects.filter(
                candidate__Email=request.data["email"]).first()
            selectedcandidateserializer = selectedcandidatesgridviewSerializer(
                selectedcandidate)
            return Response(selectedcandidateserializer.data)
        except Exception as ex:
            return Response(str(ex)+"error while fetching selcted candidate data",status=status.HTTP_400_BAD_REQUEST)