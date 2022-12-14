from django.shortcuts import render
from rest_framework.views import APIView

from jobpost.models.jobpostmodel import JobPost
from jobpost.serializers import JobPostDetailsGridSerializer, JobPostDetailsPostSerializer
from django.http.response import JsonResponse
from rest_framework import status  
from rest_framework.response import Response

# Create your views here.

class MyJobPostDetails(APIView):

    def post(self, request, format=None): 
        Jobposts = JobPost.objects.filter(UserName=request.data["UserName"]).order_by("JobPostId").reverse()
        jobpostdetailsgrid_serializer = JobPostDetailsGridSerializer(Jobposts, many=True)
        return Response(jobpostdetailsgrid_serializer.data)

