from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from jobpost.models.jobpostuserrolesmodel import JobPostUserRolesModel
from rest_framework.response import Response
from rest_framework import status 

from jobpost.serializers import JobPostUserRolesModelSerializer

class usersByGroup(APIView):

    def post(self, request, format=None): 
        # roleName = request.data['RoleName']
        jobPostUserRoles = JobPostUserRolesModel.objects.all()
        JobPostUserRoles_serializer = JobPostUserRolesModelSerializer(jobPostUserRoles, many=True)
        # if JobPostUserRoles_serializer.is_valid():
        return Response(JobPostUserRoles_serializer.data)
        # return Response(JobPostUserRoles_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)    