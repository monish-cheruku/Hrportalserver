from asyncio.windows_events import NULL
from dataclasses import fields
import json
from pyexpat import model
from rest_framework import serializers
from .models import AvgCTC

class  AvgCTCSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvgCTC
        fields = '__all__'
    

    def validate_ServiceLineId(self, value):
        # I assumed that you will that the string value, is a JSON object.
        # entered_name = json.loads(value).get('en', None)
        print(value)
        if value is None:
            raise serializers.ValidationError("ServiceLine Id is mandatory")
        #elif (value and Company.objects.filter(CompanyName=value).exists()):
          #  raise serializers.ValidationError("Company name already exists!")
        # You need to return the value in after validation.
        return value 

    def validate_ExperienceLevelId(self, value):
        # I assumed that you will that the string value, is a JSON object.
        # entered_name = json.loads(value).get('en', None)
        print(value)
        if value is None:
            raise serializers.ValidationError("ExperienceLevel Id should not be empty")
        #elif (value and Company.objects.filter(CompanyName=value).exists()):
          #  raise serializers.ValidationError("Company name already exists!")
        # You need to return the value in after validation.
        return value 