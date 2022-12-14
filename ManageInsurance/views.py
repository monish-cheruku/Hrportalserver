from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response  
from rest_framework import status  
from .models import Insurance
from .serializers import InsuranceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1

class InsuranceApi(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None): 
        insurance = Insurance.objects.all()
        insurance_serializer = InsuranceSerializer(insurance, many=True)
        return Response(insurance_serializer.data)
    
    def post(self, request, format=None):
        # insurance_data = JSONParser().parse(request)
        insurance_serializer = InsuranceSerializer(data=request.data)
        if insurance_serializer.is_valid():
            insurance_serializer.save()
            # return Response({"status": "success", "data": insurance_serializer.data}, status=status.HTTP_200_OK)  
            return Response(Messages1.Add_Scfl)
        return Response(insurance_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
        # else:
            # return Response({"status": "error", "data": insurance_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self, request, format=None):
        # insurance_data = JSONParser().parse(request)
        insurance =  Insurance.objects.get(InsuranceAccidentLimitId=request.data['InsuranceAccidentLimitId'])
        insurance_serializer = InsuranceSerializer(insurance, data=request.data)
        if insurance_serializer.is_valid():
            insurance_serializer.save()
            return Response(Messages1.Upd_Scfl)
        return Response(insurance_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
       # return JsonResponse("Failed To update", safe=False)
    
    def delete(self, request, pk, format=None):      
        insurance =  Insurance.objects.get(InsuranceAccidentLimitId=pk)    
        insurance.delete()
        return Response(Messages1.Del_Scfl)