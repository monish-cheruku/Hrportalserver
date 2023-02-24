from django.shortcuts import render
from .models import DepartmentInformation
from django.http.response import JsonResponse
from rest_framework.response import Response  
from rest_framework import status  
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1
from rest_framework.decorators import APIView
from .serializers import DepartmentSerializer
# Create your views here.

class departmentApi(APIView):
    serializer_class = DepartmentSerializer
    def get(self, request, format=None): 
        info = DepartmentInformation.objects.all()
        info_serializer = DepartmentSerializer(info, many=True)
        return JsonResponse(info_serializer.data, safe=False)
    
    def post(self, request, format=None):
        info_serializer = DepartmentSerializer(data=request.data)
        if info_serializer.is_valid():
            info_serializer.save()
            return Response(Messages1.ADD_SCFL)
        return Response(info_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
       
    
    def put(self, request, format=None):
        info =  DepartmentInformation.objects.get(Id=request.data['Id'])
        info_serializer = DepartmentSerializer(info, data=request.data)
        if info_serializer.is_valid():
            info_serializer.save()
            return Response(Messages1.UPD_SCFL)
        return Response(info_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):      
        info =  DepartmentInformation.objects.get(Id=pk)    
        info.delete()
        return Response(Messages1.DEL_SCFL)
       

