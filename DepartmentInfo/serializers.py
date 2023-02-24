from rest_framework import serializers
from .models import DepartmentInformation

class  DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentInformation
        fields = '__all__'
    