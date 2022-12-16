from rest_framework import serializers
from HRproj.settings import MEDIA_ROOT, MEDIA_URL

from CandidateFeedback.models.Candidate_Feedback_Model import Candidate_Feedback
from CandidateFeedback.models.Feedback_Category_Model import Feedback_Category

class FeedbackFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback_Category
        fields="__all__"
