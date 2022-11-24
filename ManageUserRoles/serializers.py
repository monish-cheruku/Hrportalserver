from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'groups')
        # fields = '__all__'

class PostUserSerializer(serializers.ModelSerializer):
    #groups = serializers.ListField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'groups')


