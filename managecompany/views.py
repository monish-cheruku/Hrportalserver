from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response  
from rest_framework import status  
from managecompany.models import Company
from managecompany.serializers import CompanySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

class companyApi(GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer
    def get(self, request, format=None): 
        companies = Company.objects.all()
        company_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(company_serializer.data, safe=False)
    
    def post(self, request, format=None):
        # company_data = JSONParser().parse(request)
        company_serializer = CompanySerializer(data=request.data)
        if company_serializer.is_valid():
            company_serializer.save()
            # return Response({"status": "success", "data": company_serializer.data}, status=status.HTTP_200_OK)  
            return Response("Added Successfully")
        return Response(company_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
        # else:
            # return Response({"status": "error", "data": company_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self, request, format=None):
        # company_data = JSONParser().parse(request)
        companies =  Company.objects.get(CompanyId=request.data['CompanyId'])
        company_serializer = CompanySerializer(companies, data=request.data)
        if company_serializer.is_valid():
            company_serializer.save()
            return Response("Updated Successfully")
        return Response(company_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
       # return JsonResponse("Failed To update", safe=False)
    
    def delete(self, request, pk, format=None):      
        companies =  Company.objects.get(CompanyId=pk)    
        companies.delete()
        return Response("Deleted Successfully")
       

