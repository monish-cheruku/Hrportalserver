from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response  
from rest_framework import status  
from .models import Experience
from .serializers import ExperienceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1


class ExperienceApi(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None): 
        experiences = Experience.objects.all()
        experience_serializer = ExperienceSerializer(experiences, many=True)
        return JsonResponse(experience_serializer.data, safe=False)
    
    def post(self, request, format=None):
        # experience_data = JSONParser().parse(request)
        experience_serializer = ExperienceSerializer(data=request.data)
        if experience_serializer.is_valid():
            experience_serializer.save()
            # return Response({"status": "success", "data": experience_serializer.data}, status=status.HTTP_200_OK)  
            return Response(Messages1.Add_Scfl)
        return Response(experience_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
        # else:
            # return Response({"status": "error", "data": experience_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self, request, format=None):
        # experience_data = JSONParser().parse(request)
        experiences =  Experience.objects.get(ExperienceLevelId=request.data['ExperienceLevelId'])
        experience_serializer = ExperienceSerializer(experiences ,data=request.data)
        if experience_serializer.is_valid():
            experience_serializer.save()
            return Response(Messages1.Upd_Scfl)
        return Response(experience_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
       # return JsonResponse("Failed To update", safe=False)
    
    def delete(self, request, pk, format=None):      
        experiences =  Experience.objects.get(ExperienceLevelId=pk)    
        experiences.delete()
        return Response(Messages1.Del_Scfl)

       