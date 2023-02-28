from candidate.models.selected_Candidates_Model import Selected_Candidates
from rest_framework.response import Response
from rest_framework import status
from candidate.models.selected_Candidates_Model import Selected_Candidates
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from selectedcandidate.models.Candidatedducationaldetails import CandidateEducationalDetails
from selectedcandidate.models.Candidatefamilydetails import CandidateFamilyDetails
from selectedcandidate.models.Documentsupload import CandidateDocumentsUpload


class Candidateinfoclearance(ModelViewSet):
    @action(detail=True, methods=["post"])
    def getallcandidateinfoclearance(self, request, format=None):
        try:
            res={
                'validation':True,
                'messages':[]
            }
            
            ceduob=CandidateEducationalDetails.objects.filter(selectedCandidateId_id=request.data["selectedcandidateid"])
           
            if ceduob.__len__()==0:
                res["validation"]=False
                res["messages"].append("Please Complete Educational Details Section")
          
            cfamilyob=CandidateFamilyDetails.objects.filter(selectedCandidateId_id=request.data["selectedcandidateid"])
           
            if cfamilyob.__len__()==0:
                res["validation"]=False
                res["messages"].append("Please Complete Family Details Section")

            otherdocsob=CandidateDocumentsUpload.objects.filter(selectedcandidate=request.data["selectedcandidateid"])
            if otherdocsob.filter(detailtype="Photograph").__len__()<1:
                res["validation"]=False
                res["messages"].append("Please Upload Your Photograph")

            if otherdocsob.filter(detailtype="Pan").__len__()<1:
                res["validation"]=False
                res["messages"].append("Please Upload Your Pan")

            if otherdocsob.filter(detailtype="Aadhar").__len__()<1:
                res["validation"]=False
                res["messages"].append("Please Upload Your Aadhar")
            if otherdocsob.filter(detailtype="Signedofferletter").__len__()<1:
                res["validation"]=False
                res["messages"].append("Please Upload Your Signedofferletter")

            # if otherdocsob.filter(detailtype="Passport").__len__()<1:
            #     res["validation"]=False
            #     res["messages"].append("Please Upload Your Passport")
        


            # documentuploadserializer = Documentuploadserializer(
            #     data=request.data, context=request.FILES)
            # if documentuploadserializer.is_valid():
            #     duo = documentuploadserializer.save()

            return Response(res, status=status.HTTP_200_OK)
        except Exception as exp:
            # exp.with_traceback()
            return Response(exp, status=status.HTTP_400_BAD_REQUEST)
