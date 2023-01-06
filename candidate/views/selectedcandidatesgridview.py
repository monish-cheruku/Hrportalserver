from candidate.models.selected_Candidates_Model import Selected_Candidates
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from candidate.models.candidatemodel import Candidate
from jobpost.models.jobpostapprovalmodel import JobPostApproval
from candidate.serializers import selectedcandidatesgridviewSerializer
class selectedcandidatesgridview(APIView):
    def post(self,request,format=None):
        role=[]
        role=request.data["RoleName"]
        username=request.data["username"]
        selectedcandidatesarr=[]
        res=[]
        product_qs=Selected_Candidates.objects.none()
        try:
            if Constants1.ROLE_HR in role: 
                selectedcandidates = Selected_Candidates.objects.all()
                product_qs=product_qs.union(selectedcandidates)

            if Constants1.ROLE_RECRUITER in role:
                product_qs=product_qs.union(Selected_Candidates.objects.filter(candidate__HRUserName=username))

            if Constants1.ROLE_HM in role:

                product_qs=product_qs.union(Selected_Candidates.objects.filter(candidate__Jobpost__UserName=username))
     
            if Constants1.ROLE_BH in role:

                jparr=[]
                jobpostapprovals=JobPostApproval.objects.filter(approverName=username,Stage_id=1,role_id=2)
                for jp in jobpostapprovals:
                    jparr.append(jp.jobpost.JobPostId)
                product_qs=product_qs.union(Selected_Candidates.objects.filter(candidate__Jobpost__JobPostId__in=jparr))
            return Response(selectedcandidatesgridviewSerializer(product_qs, many=True).data)  
        except Exception as err:
            return Response(str(err)+"error while fetching selcted candidates",status=status.HTTP_400_BAD_REQUEST)
