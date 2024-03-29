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
from django.contrib.auth.models import User, Group
from   . import ldapfun
from Scheduler.Task1 import ManageADUsers

from decouple import config
# Create your views here.

class LoginApi(APIView):

    def post(self, request, format=None): 
        # loginSerializer = LoginSerializer(data=request.data)
        try:
            user = User.objects.filter(username= request.data['User_name'],is_active=True).first()
            # user = authenticate(username=request.data['User_name'], password =request.data['User_name'] )
            
            if user is not None:
                groupsdetails =user.groups.all()
                if groupsdetails.contains(Group.objects.filter(name = 'Candidate').first() ):
                    user = authenticate(username=request.data['User_name'], password =request.data['password'] )
                    if user is None:
                        return Response(Messages1.UNF, status=status.HTTP_403_FORBIDDEN)          
                else:
                    if config("AD_AUTHENTICATION")=="True":
                    #    Active directory validation
                        print("executing ldap fun")
                        res=ldapfun.connecttoad(user.email,request.data['password'] )
                        if res==True:
                            print("")
                        else:
                            return Response("User Not Found", status=status.HTTP_403_FORBIDDEN)
                        # ManageADUsers()
                      
                userserializer =  UserSerializer(user)
                return Response(userserializer.data, status=status.HTTP_200_OK)
                # l = user.groups.values_list('name',flat = True) # QuerySet Object
                # l_as_list = list(l)   
                # print(l_as_list)
            else:
                return Response(Messages1.UNF, status=status.HTTP_403_FORBIDDEN)
        except Exception as ex:
                return Response(Messages1.UNF, status=status.HTTP_403_FORBIDDEN)


            

    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }