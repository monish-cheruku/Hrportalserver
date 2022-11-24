from asyncio.windows_events import NULL
from dataclasses import fields
import json
from pyexpat import model
from rest_framework import serializers
from .models import Industry

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'
    

    def validate_IndustryName(self, value):
        print(value)
        if value is None:
            raise serializers.ValidationError("Industry name should not be empty")
        return value   