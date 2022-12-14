from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response  
from rest_framework import status  
from .models import BusinessUnit
from .serializers import BusinessUnitSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1


class BusinessUnitApi(GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None): 
        businessunits = BusinessUnit.objects.all()
        businessunit_serializer = BusinessUnitSerializer(businessunits, many=True)
        return JsonResponse(businessunit_serializer.data, safe=False)

    def post(self, request, format=None):
        # company_data = JSONParser().parse(request)
        businessunit_serializer = BusinessUnitSerializer(data=request.data)
        if businessunit_serializer.is_valid():
            businessunit_serializer.save()
            # return Response({"status": "success", "data": businessunit_serializer.data}, status=status.HTTP_200_OK)  
            return Response(Messages1.Add_Scfl)
        return Response(businessunit_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
        # else:
            # return Response({"status": "error", "data": businessunit_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self, request, format=None):
        # businessunit_data = JSONParser().parse(request)
        businessunits =  BusinessUnit.objects.get(BusinessUnitId=request.data['BusinessUnitId'])
        businessunit_serializer = BusinessUnitSerializer(businessunits ,data=request.data)
        if businessunit_serializer.is_valid():
            businessunit_serializer.save()
            return Response(Messages1.Upd_Scfl)
        return Response(businessunit_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
       # return JsonResponse("Failed To update", safe=False)
    
    def delete(self, request, pk, format=None):      
        businessunits =  BusinessUnit.objects.get(BusinessUnitId=pk)    
        
        businessunits.delete()
        return Response(Messages1.Del_Scfl)
       

