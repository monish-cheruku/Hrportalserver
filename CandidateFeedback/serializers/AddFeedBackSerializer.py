from rest_framework import serializers
from CandidateFeedback.models.Candidate_Feedback_Model import Candidate_Feedback
from CandidateFeedback.models.Feedback_Category_Model import Feedback_Category

class FeedbackBulkCreateSerializer(serializers.ListSerializer):  
    def create(self, validated_data):  
        product_data = [Candidate_Feedback(**item) for item in validated_data]  
        return Candidate_Feedback.objects.bulk_create(product_data)  
  
  
class AddFeedBackSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Candidate_Feedback  
        fields ="__all__"
        # read_only_fields = ['id',]  
        list_serializer_class = FeedbackBulkCreateSerializer