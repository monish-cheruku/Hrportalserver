from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response  
from rest_framework import status  
from .models import ServiceLine
from .serializers import ServiceLineSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ServiceLineApi(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None): 
        servicelines = ServiceLine.objects.all()
        serviceline_serializer = ServiceLineSerializer(servicelines, many=True)
        return Response(serviceline_serializer.data)
    
    def post(self, request, format=None):
        # serviceline_data = JSONParser().parse(request)
        serviceline_serializer = ServiceLineSerializer(data=request.data)
        if serviceline_serializer.is_valid():
            serviceline_serializer.save()
            # return Response({"status": "success", "data": serviceline_serializer.data}, status=status.HTTP_200_OK)  
            return Response("Added Successfully")
        return Response(serviceline_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
        # else:
            # return Response({"status": "error", "data": serviceline_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self, request, format=None):
        # serviceline_data = JSONParser().parse(request)
        servicelines =  ServiceLine.objects.get(ServiceLineId=request.data['ServiceLineId'])
        serviceline_serializer = ServiceLineSerializer(servicelines, data=request.data)
        if serviceline_serializer.is_valid():
            serviceline_serializer.save()
            return Response("Updated Successfully")
        return Response(serviceline_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
       # return JsonResponse("Failed To update", safe=False)
    
    def delete(self, request, pk, format=None):      
        servicelines =  ServiceLine.objects.get(ServiceLineId=pk)    
        servicelines.delete()
        return Response("Deleted Successfully")
       

