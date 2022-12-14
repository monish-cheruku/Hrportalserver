import logging
import this
from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
# from ms_active_directory import ADDomain
from rest_framework.response import Response
from rest_framework import status  

from login.serializers import LoginSerializer, UserSerializer
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1

# Create your views here.

class LoginApi(APIView):

    def post(self, request, format=None): 
        # loginSerializer = LoginSerializer(data=request.data)
        user = authenticate(username=request.data['User_name'], password =request.data['User_name'] )
        userserializer =  UserSerializer(user)
        if user is not None:
            return Response(userserializer.data, status=status.HTTP_200_OK)
            # l = user.groups.values_list('name',flat = True) # QuerySet Object
            # l_as_list = list(l)   
            # print(l_as_list)
        else:
            return Response(Messages1.UNF, status=status.HTTP_403_FORBIDDEN)

            

    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }