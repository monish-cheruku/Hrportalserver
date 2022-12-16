from rest_framework import serializers


from CandidateFeedback.models.Candidate_Feedback_Model import Candidate_Feedback
from CandidateFeedback.models.Feedback_Category_Model import Feedback_Category
from CandidateFeedback.serializers.FeedbackFieldsSerializer import FeedbackFieldsSerializer

class CandidateFeedBacksSerializer(serializers.ModelSerializer):
    interviewtype=serializers.CharField(read_only=True, source="FeedbackCategory.InterviewType")
    feedbackcategory=serializers.CharField(read_only=True, source="FeedbackCategory.FeedbackCategory")
    # Feedback_Category_name=Feedback_Category.objects.filter(Feedback_Category_ID=)
    # Feedback_Category_name=FeedbackFieldsSerializer(many=True)
    # Feedback_Category_name=serializers.PrimaryKeyRelatedField(many=True)
    # Interview_Type=serializers.CharField(read_only=True, source="Feedback_Category.Interview_Type")
    # Feedback_Category=serializers.CharField(read_only=True, source="Feedback_Category.Feedback_Category")
    # Feedback_Category=serializers.SlugRelatedField(many=True, 
    # read_only=True,
    # slug_field="Feedback_Category.Feedback_Category")

    # pesticides = serializers.SerializerMethodField()

    # def get_pesticides(self, disease):
    #     feedback = Feedback_Category.objects.filter(treatments__disease=disease)
    #     return PesticideSerializer(feedback, many=True).data

    class Meta:
        model=Candidate_Feedback
        fields="__all__"