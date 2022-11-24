from asyncio.windows_events import NULL
from dataclasses import fields
import json
from pyexpat import model
from rest_framework import serializers
from .models import Designation

class  DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
    

    def validate_DesignationName(self, value):
        # I assumed that you will that the string value, is a JSON object.
        # entered_name = json.loads(value).get('en', None)
        print(value)
        if value is None:
            raise serializers.ValidationError("Designation name should not be empty")
        #elif (value and Company.objects.filter(DesignationName=value).exists()):
          #  raise serializers.ValidationError("Designation name already exists!")
        # You need to return the value in after validation.
        return value   