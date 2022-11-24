from asyncio.windows_events import NULL
from dataclasses import fields
import json
from pyexpat import model
from rest_framework import serializers
from ManageAdUsers.models import AdUsers

class AdUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdUsers
        fields = '__all__'
    
    def validate_UserName(self, value):
        print(value)
        if value is None:
            raise serializers.ValidationError("User name is mandatory")
        return value 
    
    def validate_FirstName(self, value):
        print(value)
        if value is None:
            raise serializers.ValidationError("First name should not be empty")
        return value 

    def validate_LastName(self, value):
        print(value)
        if value is None:
            raise serializers.ValidationError("Last name should not be empty")
        return value 

    def validate_Email(self, value):
        print(value)
        if value is None:
            raise serializers.ValidationError("Email is mandatory")
        return value   