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
                # res =res+ selectedcandidatesgridviewSerializer(selectedcandidates, many=True).data
                product_qs=product_qs | selectedcandidatesgridviewSerializer(selectedcandidates, many=True)

            if Constants1.ROLE_RECRUITER in role:
                # queryset = Selected_Candidates.prefetch_related('reading_group', 'reading_group__users', 'reading_group__owner') 
                # print(Selected_Candidates.Candidate_ID.get_object())
                # HB=Candidate.objects.prefetch_related('Selected_Candidates_set')
                # selectedcandidates1 = Selected_Candidates.objects.all()
                # for s in selectedcandidates1:
                #     if s.candidate.HRUserName==username:
                #         selectedcandidatesarr.append(s)
                # print(selectedcandidatesarr)
                product_qs=product_qs.union(Selected_Candidates.objects.filter(candidate__HRUserName=username))




                res =  selectedcandidatesgridviewSerializer(product_qs, many=True)
            if Constants1.ROLE_HM in role:
                # queryset = Selected_Candidates.prefetch_related('reading_group', 'reading_group__users', 'reading_group__owner') 
                # print(Selected_Candidates.Candidate_ID.get_object())
                # selectedcandidates1 = Selected_Candidates.objects.all()
                # for s in selectedcandidates1:
                #     if s.candidate.Jobpost.UserName==username:
                #         selectedcandidatesarr.append(s)
                # print(selectedcandidatesarr)
                # product_qs =Selected_Candidates.objects.filter(candidate__Jobpost__UserName=username)
                res=product_qs.union(Selected_Candidates.objects.filter(candidate__Jobpost__UserName=username))
                


                # res = res+selectedcandidatesgridviewSerializer(product_qs, many=True).data
            if Constants1.ROLE_BH in role:
                # queryset = Selected_Candidates.prefetch_related('reading_group', 'reading_group__users', 'reading_group__owner') 
                # print(Selected_Candidates.Candidate_ID.get_object())
                # selectedcandidates1 = Selected_Candidates.objects.all()
                # for s in selectedcandidates1:
                #     if s.candidate.Jobpost.UserName==username:
                #         selectedcandidatesarr.append(s)
                # print(selectedcandidatesarr)
                jparr=[]
                jobpostapprovals=JobPostApproval.objects.filter(approverName=username,Stage_id=1,role_id=2)
                for jp in jobpostapprovals:
                    jparr.append(jp.jobpost.JobPostId)
                # product_qs = Selected_Candidates.objects.filter(candidate__Jobpost__JobPostId__in=jparr)

                res1 =Selected_Candidates.objects.filter(candidate__Jobpost__JobPostId__in=jparr)
                # res =selectedcandidatesgridviewSerializer(product_qs, many=True).data
                product_qs=res.union(res1)


            # product_qs=product_qs.distinct()
            return Response(selectedcandidatesgridviewSerializer(product_qs, many=True).data)  
        except Exception as err:
            return Response(str(err)+"error while fetching selcted candidates",status=status.HTTP_400_BAD_REQUEST)
