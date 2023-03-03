from rest_framework.response import Response
from rest_framework import status
from candidate.models.selected_Candidates_Model import  Selected_Candidates
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from selectedcandidate.models.Candidatepfdetails import CandidatePfDetails
from selectedcandidate.Serializers import candidatePFdetailgetSerializer

class PFdetailsview(ModelViewSet):
    @action(detail=True,methods=["post"])
    def createPFdetail(self,request,format=None):
        try:
            # CandidatePersonalInfo.objects.all()
            CandidatePfDetails.objects.create(
            selectedcandidateid=Selected_Candidates.objects.filter(Selected_Candidate_ID=request.data["selectedcandidateid"]).first(),
            PreviousCompanyUAN = request.data["PreviousCompanyUAN"],
            PreviousMemberId = request.data["PreviousMemberId"],
            MemberNameAsPerAadhar = request.data["MemberNameAsPerAadhar"],
            AADHAR = request.data["AADHAR"],
            DateOfBirth = request.data["DateOfBirth"],
            Date_Of_Joining = request.data["Date_Of_Joining"],
            Gender = request.data["Gender"],
            FatherOrHusbandName = request.data["FatherOrHusbandName"],
            Relation = request.data["Relation"],
            Marital_status = request.data["Marital_status"],
            InternationalWorker = request.data["InternationalWorker"],
            ContactNumber = request.data["ContactNumber"],
            Email = request.data["Email"],
            Nationality = request.data["Nationality"],
            wages = request.data["wages"],
            Qualification = request.data["Qualification"],
            CountryOfOrigin = request.data["CountryOfOrigin"],
            PassportNumber = request.data["PassportNumber"],
            PassportValidFrom = request.data["PassportValidFrom"],
            PassportValidTill = request.data["PassportValidTill"],
            PhysicalHandicap = request.data["PhysicalHandicap"],
            AccountNumber = request.data["AccountNumber"],
            IFSCcode = request.data["IFSCcode"],
            NameAsPerBank = request.data["NameAsPerBank"],
            PAN = request.data["PAN"],
            NameAsPerPan = request.data["NameAsPerPan"],   
            )

            return Response("PF detail created",status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return  Response(e,status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True,methods=["post"])
    def updatePFdetail(self,request,format=None):
        try:

            CandidatePfDetails.objects.filter(Id=request.data["Id"]).update(
            selectedcandidateid=Selected_Candidates.objects.filter(Selected_Candidate_ID=request.data["selectedcandidateid"]).first(),
            PreviousCompanyUAN = request.data["PreviousCompanyUAN"],
            PreviousMemberId = request.data["PreviousMemberId"],
            MemberNameAsPerAadhar = request.data["MemberNameAsPerAadhar"],
            AADHAR = request.data["AADHAR"],
            DateOfBirth = request.data["DateOfBirth"],
            Date_Of_Joining = request.data["Date_Of_Joining"],
            Gender = request.data["Gender"],
            FatherOrHusbandName = request.data["FatherOrHusbandName"],
            Relation = request.data["Relation"],
            Marital_status = request.data["Marital_status"],
            InternationalWorker = request.data["InternationalWorker"],
            ContactNumber = request.data["ContactNumber"],
            Email = request.data["Email"],
            Nationality = request.data["Nationality"],
            wages = request.data["wages"],
            Qualification = request.data["Qualification"],
            CountryOfOrigin = request.data["CountryOfOrigin"],
            PassportNumber = request.data["PassportNumber"],
            PassportValidFrom = request.data["PassportValidFrom"],
            PassportValidTill = request.data["PassportValidTill"],
            PhysicalHandicap = request.data["PhysicalHandicap"],
            AccountNumber = request.data["AccountNumber"],
            IFSCcode = request.data["IFSCcode"],
            NameAsPerBank = request.data["NameAsPerBank"],
            PAN = request.data["PAN"],
            NameAsPerPan = request.data["NameAsPerPan"],   
            )

            return  Response("PF details updated succesfully",status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True,methods=["post"])
    def getPFdetails(self,request,format=None):
        try:

            pfdo=CandidatePfDetails.objects.filter(selectedcandidateid=request.data["selectedcandidateid"]).first()
            pfdos=candidatePFdetailgetSerializer(pfdo,many=False).data
            return  Response(pfdos,status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)
    
    def deletePFdetail(self,request,format=None):
        try:

            pfdo=CandidatePfDetails.objects.filter(Id=request.data["Id"]).first()
            pfdo.delete()
            return  Response("Deleted Sucessfully",status=status.HTTP_200_OK)
        except Exception as e:
             return  Response(e,status=status.HTTP_400_BAD_REQUEST)