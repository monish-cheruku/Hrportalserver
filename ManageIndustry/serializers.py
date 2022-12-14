from asyncio.windows_events import NULL
from dataclasses import fields
import json
from pyexpat import model
from rest_framework import serializers
from .models import Industry
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'
    

    def validate_IndustryName(self, value):
        print(value)
        if value is None:
            raise serializers.ValidationError(Messages1.IN_Empty)
        return value   