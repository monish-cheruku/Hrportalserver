from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework import status  
from rest_framework.response import Response
from jobpost.models.jobpostactionmodel import JobPostActionModel

from jobpost.models.jobpostapprovalmodel import JobPostApproval
from jobpost.models.jobpostmodel import JobPost
from jobpost.serializers import JobPostActionGridSerializer, JobPostActionModelSerializer, JobPostApprovalSerializer, JobPostDetailsPostSerializer
from datetime import datetime

from managestages.models import Stage
from django.db import transaction
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1

# Create your views here.

class JobPostAction(ModelViewSet):
    @action(detail=True, methods=['post'])
    def jobpostactiondetails(self, request, format=None):     
        print(request.data)   
        jobPostActionModel = JobPostActionModel.objects.filter(ApproverName=request.data["ApproverName"]).order_by("id").reverse()
        JobPostActionModel_serializer = JobPostActionModelSerializer(jobPostActionModel, many=True)
        return Response(JobPostActionModel_serializer.data)
        # return Response(JobPostActionModel_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST) 
    @action(detail=True, methods=['post'])
    def jobpostactionsubmit(self, request, format=None): 
        jobPostApprovalId =  request.data['JobPostApprovalId']
        jobPostId =  request.data['JobPostId']
        approvalStatus =  request.data['ApprovalStatus']
        approvalComments =  request.data['ApprovalComments']
        response = ''
        try:
            with transaction.atomic():
                jobPostApproval =  JobPostApproval.objects.filter(jobPostApprovalId=jobPostApprovalId).update(
                    approvalDate = datetime.now(),
                    approvalStatus = approvalStatus,
                    approvalComments = approvalComments,
                )

                # JobPostApproval_serializer = JobPostApprovalSerializer(jobPostApproval)
                # if JobPostApproval_serializer.is_valid():
                #     jobPostApprovalupdated = JobPostApproval_serializer.save()
                if jobPostApproval is not None:
                    if (approvalStatus == Constants1.STAGE_A):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_PP).first()
                        response = Messages1.JP_APP_SCFL 
                    elif (approvalStatus == Constants1.STAGE_R):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_R).first()
                        response = Messages1.JP_RJCTD
                    print(stage.StageId)
                    jobpost =  JobPost.objects.filter(JobPostId=jobPostId).update(
                        Stage =  stage   
                    )
                    print(jobpost)
                    return Response(response, status=status.HTTP_200_OK)            
                #     jobpost.Stage = stage                
                #     JobPostDetailsPost_serializer = JobPostDetailsPostSerializer(jobpost)
                #     if JobPostDetailsPost_serializer.is_valid():
                #         JobPostDetailsPost_serializer.save()
                #         return Response("Submitted Successfully")
                #     return Response("Exception while approve the job post details"+str(JobPostDetailsPost_serializer.errors), status=status.HTTP_400_BAD_REQUEST) 
                # return Response(JobPostApproval_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        except Exception as exp:
            return Response(Messages1.ERR_APP_JP_DTLS+str(exp), status=status.HTTP_400_BAD_REQUEST)        