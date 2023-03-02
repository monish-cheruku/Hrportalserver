from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from candidate.models.Feedback_Category_Model import Feedback_Category
from candidate.serializers import FeedbackFieldsSerializer
from candidate.models.candidatemodel  import Candidate
from ManageLocation.models import Location
class Hrupdatecandidate(APIView):
    def post(self,request,format=None):
        try:
            # feedbackfields = Feedback_Category.objects.filter(Stage=request.data["stagename"])
            # res = FeedbackFieldsSerializer(feedbackfields, many=True)
            canob=Candidate.objects.filter(CandidateId=request.data["CandidateId"]).first()
            print(canob)

            canob.CandidateId=request.data["CandidateId"]
            canob.NegotiatedCTC=request.data["NegotiatedCTC"]
            canob.EmploymentType=request.data["EmploymentType"]
            canob.Location=Location.objects.filter(LocationId= request.data["Location"] ).first()
            canob.ModifiedBy=request.data["ModifiedBy"]
            canob.save()

            return Response("updated Candidate details", status=status.HTTP_200_OK)    
        except Exception as e:
            return Response(" Candidate Update Failed",status=status.HTTP_400_BAD_REQUEST)
