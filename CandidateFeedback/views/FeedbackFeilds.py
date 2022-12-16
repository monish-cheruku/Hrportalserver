from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from CandidateFeedback.models.Feedback_Category_Model import Feedback_Category
from CandidateFeedback.models.Candidate_Feedback_Model import Candidate_Feedback
from CandidateFeedback.serializers.FeedbackFieldsSerializer import FeedbackFieldsSerializer
class FeedbackFields(APIView):
    def post(self,request,format=None):
        try:
            feedbackfields = Feedback_Category.objects.filter(InterviewType=request.data["Interview_Round"])
            res = FeedbackFieldsSerializer(feedbackfields, many=True)

            return Response(res.data)    
        except:
            return Response("failed",status=status.HTTP_400_BAD_REQUEST)
