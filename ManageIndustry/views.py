from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response  
from rest_framework import status  
from .models import Industry
from .serializers import IndustrySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1


class IndustryApi(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None): 
        industries = Industry.objects.all()
        industry_serializer = IndustrySerializer(industries, many=True)
        return JsonResponse(industry_serializer.data, safe=False)
    
    def post(self, request, format=None):
        industry_serializer = IndustrySerializer(data=request.data)
        if industry_serializer.is_valid():
            industry_serializer.save()
            return Response(Messages1.ADD_SCFL)
        return Response(industry_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        industries =  Industry.objects.get(IndustryId=request.data['IndustryId'])
        industry_serializer = IndustrySerializer(industries, data=request.data)
        if industry_serializer.is_valid():
            industry_serializer.save()
            return Response(Messages1.UPD_SCFL)
        return Response(industry_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):      
        designations =  Industry.objects.get(IndustryId=pk)    
        designations.delete()
        return Response(Messages1.DEL_SCFL)
       
