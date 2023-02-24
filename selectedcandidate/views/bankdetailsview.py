from rest_framework.response import Response
from rest_framework import status
from candidate.models.selected_Candidates_Model import  Selected_Candidates
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from selectedcandidate.models.Candidatebankdetails import CandidateBankDetails
from selectedcandidate.Serializers import candidatebankdetailgetSerializer
from selectedcandidate.Serializers import bankdetailupdaeSerializer

class bankdetailsview(ModelViewSet):
    @action(detail=True,methods=["post"])
    def createbankdetail(self,request,format=None):
        try:
            # CandidatePersonalInfo.objects.all()
            CandidateBankDetails.objects.create(
            selectedcandidateid=Selected_Candidates.objects.filter(Selected_Candidate_ID=request.data["selectedcandidateid"]).first(),
            BankName=request.data["BankName"],
            AccountNumber=request.data["AccountNumber"],
            BranchName=request.data["BranchName"],
            IFSCcode=request.data["IFSCcode"],
            BankPassbook=request.data["BankPassbook"],
            )
            return  Response("Bank detail created",status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return  Response(e,status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True,methods=["post"])
    def updatebankdetail(self,request,format=None):
        try:
            # CandidateBankDetails.objects.filter(Id=request.data["Id"]).update(
            #    selectedcandidateid=Selected_Candidates.objects.filter(Selected_Candidate_ID=request.data["selectedcandidateid"]).first(),
            #    BankName=request.data["BankName"],
            #    AccountNumber=request.data["AccountNumber"],
            #    BranchName=request.data["BranchName"],
            #    IFSCcode=request.data["IFSCcode"],
            #    # hasbankpassbook =False if request.data["BankPassbook"] is None else True
            #    BankPassbook=request.data["BankPassbook"] if request.data["BankPassbook"] is not  None else print() 
            #    # BankPassbook=request.data["BankPassbook"],
            
            # )
            bankdetails=CandidateBankDetails.objects.filter(Id=request.data["Id"]).first()
            # if request.data["BankPassbook"] is None:
            #     bankdetailupdateserializer=candidatebankdetailupdateSerializer(bankdetails,data=request.data)
            # else:
            bankdetailupdateserializer=bankdetailupdaeSerializer(bankdetails,data=request.data)
            if bankdetailupdateserializer.is_valid():
                bankdetailupdateserializer.save()
                return  Response("Bank details updated succesfully",status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True,methods=["post"])
    def getbankdetails(self,request,format=None):
        try:

            bdo=CandidateBankDetails.objects.filter(selectedcandidateid=request.data["selectedcandidateid"]).first()
            bdos=candidatebankdetailgetSerializer(bdo,many=False).data
            return  Response(bdos,status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)
    
    def deletebankdetail(self,request,format=None):
        try:

            bdo=CandidateBankDetails.objects.filter(Id=request.data["Id"]).first()
            bdo.delete()
            return  Response("Deleted Sucessfully",status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)