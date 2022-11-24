from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from ManageAdUsers.serializers import AdUsersSerializer
from .models import AdUsers

class UsersApi(APIView):

     def get(self, request, format=None): 
        users = AdUsers.objects.all()
        user_serializer = AdUsersSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

     def post(self, request, format=None):
        user_serializer = AdUsersSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save() 
            return Response("Added Successfully")
        return Response(user_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)

     def put(self, request, format=None):
        users = AdUsers.objects.get(Id=request.data['Id'])
        user_serializer = AdUsersSerializer(users, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response("Updated Successfully")
        return Response(user_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)