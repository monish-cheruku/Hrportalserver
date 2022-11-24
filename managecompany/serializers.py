from asyncio.windows_events import NULL
from dataclasses import fields
import json
from pyexpat import model
from rest_framework import serializers
from managecompany.models import Company

class  CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
    

    def validate_CompanyName(self, value):
        # I assumed that you will that the string value, is a JSON object.
        # entered_name = json.loads(value).get('en', None)
        print(value)
        if value is None:
            raise serializers.ValidationError("Company name should not be empty")
        #elif (value and Company.objects.filter(CompanyName=value).exists()):
          #  raise serializers.ValidationError("Company name already exists!")
        # You need to return the value in after validation.
        return value   
