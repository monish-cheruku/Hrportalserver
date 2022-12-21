from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from CandidateFeedback.serializers.AddFeedBackSerializer import AddFeedBackSerializer
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1
from HRproj.util.Messages.HR_WorkFlow_Messages import Messages1
from candidate.models.candidateapprovalmodel import CandidateApprovalModel
from candidate.models.candidatemodel import Candidate
from django.db import transaction
import django_filters
from datetime import datetime
from managestages.models import Stage

# class AddFeedBack(APIView):
#     def post(self,request,format=None):
#         try:
#             print("working")
#             print(request.data)
#             res={"data":"working"}
#             return Response(res.data)
#         except:
#             return Response("failed",status=status.HTTP_400_BAD_REQUEST)

class AddFeedBack(generics.ListCreateAPIView):  
    # serializer_class = AddFeedBackSerializer 

    # def get_serializer(self, *args, **kwargs):  
    #     if isinstance(kwargs.get("data", {}), list):  
    #         kwargs["many"] = True  

    #     return super(AddFeedBack, self).get_serializer(*args, **kwargs) 


    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                candidateapprovalid=request.data.get("candidateapprovalid")
                candidateid=request.data.get("candidateid")
                Status=request.data.get("status")
                comments=request.data.get("comments")
                response = ''
                ca=CandidateApprovalModel.objects.filter(CandidateApprovalId=candidateapprovalid).first()
                ca.approvalStatus=Status
                ca.approvalDate=datetime.now()
                ca.approvalComments=comments ,
                print(ca)
                q = django_filters.Filter(method='my_custom_filter', label="Search")
                print(q)
                if ca is not None:
                        
                    if (Status == Constants1.SHORTLIST):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_HR_INTERVIEW).first()
                    elif (Status == Constants1.HM_HOLD):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_HM_HOLD).first()
                    elif (Status == Constants1.REJECTED):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_REJECTED).first()
                    elif (Status == Constants1.FURTHERREVIEW):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_FURTHERREVIEW).first()
                    elif (Status == Constants1.SELECTED):
                        stage = Stage.objects.filter(StageName=Constants1.STAGE_SELECTED).first()
                    
                    candiddateapprovalobject =  Candidate.objects.filter(CandidateId=candidateid).update(
                        Stage =  stage,
                       
                    )
                    
                    
                    ca.approvalComments=comments
                    
                    ca.approvalDate=datetime.now()
                    ca.save()
                else:
                    raise Exception
                
                def my_custom_filter(self, queryset, name,value):
                    return CandidateApprovalModel.objects.filter(
                    CandidateApprovalModel(Candidate=request.data.get("feedback")[0].get("Candidate")) and CandidateApprovalModel(role=7)
                    )
                class Meta:
                    model = CandidateApprovalModel
                    fields = "__all__"

                with transaction.atomic():
                    print("create met called")
                    print(request.data)
                    serializer = AddFeedBackSerializer(data=request.data.get("feedback"),many=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data)
        except Exception as exp:
            return Response(Messages1.Err_app_JP_dtls+str(exp), status=status.HTTP_400_BAD_REQUEST) 