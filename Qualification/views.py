from django.shortcuts import render
from rest_framework.views import APIView
from Qualification.models import Qualification
from django.http.response import JsonResponse
from Qualification.serializer import QualifiacationSerializer
# Create your views here.
class QualificationDetails(APIView):
    def get(self,request,format=None):
        qualificationdetails=Qualification.objects.all()
        qualificationserializer=QualifiacationSerializer(qualificationdetails,many=True)
        return JsonResponse(qualificationserializer.data,safe=False)