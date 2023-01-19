from asyncio.windows_events import NULL
from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class  LoginSerializer(serializers.ModelSerializer):
    User_name = serializers.CharField()
    Password = serializers.CharField()
    # class Meta:        
    #     fields = [
    #         "User_name",
    #         "Password"
    #     ]
class  GroupSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Group    
        fields = ['name']

class  UserSerializer(serializers.ModelSerializer):
    # groups = serializers.ListField(read_only=True, source="Group.Name")
    # groups = GroupSerializer(read_only=True, source="Group")
    # class Meta:    
    #     model = User    
    #     fields = ['username', 'first_name', 'last_name', 'email', 'groups']
    groups = GroupSerializer(many=True)
    # groupsarr=
    # def get_groups(self, obj):
    #      return obj.groups.values_list('name', flat=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            # 'date_joined',
            # 'last_login',
            # 'is_staff',
            # 'is_superuser',
            # 'is_active',
            'groups'
        ]    

