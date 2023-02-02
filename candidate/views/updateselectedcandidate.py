import decimal
import io
import os
from ManageInsurance.models import Insurance
from candidate.models.selected_Candidates_Model import Selected_Candidates
from HRproj.util.Constants.HR_WorkFlow_Constants import Constants1
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from candidate.models.candidatemodel import Candidate
from candidate.models.selected_Candidates_Model import  Selected_Candidates
from jobpost.models.jobpostapprovalmodel import JobPostApproval
from candidate.serializers import selectedcandidatesgridviewSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from ManageBand.models import Band
from ManageSubBand.models import SubBand
from ManageDesignation.models import Designation
from datetime import datetime
from docxtpl import DocxTemplate
from django.core.files.uploadedfile import SimpleUploadedFile
from HRproj.settings import MEDIA_ROOT

class updateselectedcandidate(ModelViewSet):
    @action(detail=True, methods=['post'])
    def updateselcandidate(self, request, format=None):
        try:
            selectedcandidate =  Selected_Candidates.objects.get(Selected_Candidate_ID=request.data["selectedcandidateid"])
            designation= Designation.objects.get(DesignationId=request.data['designation'])
            band=Band.objects.get(BandId=request.data['band'])
            subband=SubBand.objects.get(SubBandId=request.data['subband'])
            DateOfJoining=request.data["DateOfJoining"]
            FixedCTC=request.data["FixedCTC"]
            Isvariable = request.data["IsVariable"]
            VariablePay = request.data["VariablePay"]
            MQVariable=request.data["MQVariable"]
            Is_Eligible_annu_Mgnt_Bonus=request.data["Is_Eligible_annu_Mgnt_Bonus"]
            Is_Eligible_Joining_Bonus=request.data["Is_Eligible_Joining_Bonus"]
            IS_Eligible_Monthly_Incentive=request.data["IS_Eligible_Monthly_Incentive"]            
            if Isvariable is True:
                FinalCTC = FixedCTC+VariablePay
            elif Isvariable is False:
                FinalCTC =  FixedCTC  
            sco =  Selected_Candidates.objects.filter(Selected_Candidate_ID=request.data["selectedcandidateid"]).update(
                designation= designation,
                band=band,
                subband=subband,
                DateOfJoining=DateOfJoining,
                FixedCTC=FixedCTC,
                IsVariable = Isvariable,
                VariablePay=VariablePay,
                FinalCTC = FinalCTC,
                MQVariable=MQVariable,
                Is_Eligible_annu_Mgnt_Bonus=Is_Eligible_annu_Mgnt_Bonus,
                Is_Eligible_Joining_Bonus=Is_Eligible_Joining_Bonus,
                IS_Eligible_Monthly_Incentive=IS_Eligible_Monthly_Incentive,
                Modified_By=request.data["Modified_By"],
                Modified_On=datetime.now(),

            )
            # create offer letter from template

            # buffer = io.BytesIO() 
            # doc = DocxTemplate("Belcan_India_Offer_Letter_Template.docx")
            # context = self.getContext(selectedcandidate, designation, band, subband, DateOfJoining,
            #                       FixedCTC, Isvariable, VariablePay, MQVariable, Is_Eligible_annu_Mgnt_Bonus,
            #                       Is_Eligible_Joining_Bonus, IS_Eligible_Monthly_Incentive)
            # doc.render(context)
            # doc.save(buffer)
            # buffer.seek(0)
            # content_file = SimpleUploadedFile(selectedcandidate.candidate.CanLastName+'_'+selectedcandidate.candidate.CanFirstName+'_OfferLetter.docx', buffer.getvalue())
            # print(type(content_file))
            # sco =  Selected_Candidates.objects.get(Selected_Candidate_ID=request.data["selectedcandidateid"])

            # if os.path.exists(os.path.join(MEDIA_ROOT, str(sco.OfferLetter))):
            #     os.remove(os.path.join(MEDIA_ROOT, str(sco.OfferLetter)))

            # sco.OfferLetter= content_file
            # sco.save()            

            return  Response("OfferLetter Created",status=status.HTTP_200_OK)
        except Exception as e:
            return  Response(e,status=status.HTTP_400_BAD_REQUEST)



    @action(detail=True, methods=['post'])
    def getAnnexureDetails(self, request, format=None):
        try:
            selectedcandidate =  Selected_Candidates.objects.get(Selected_Candidate_ID=request.data["selectedcandidateid"])
            designation= Designation.objects.get(DesignationId=request.data['designation'])
            band=Band.objects.get(BandId=request.data['band'])
            subband=SubBand.objects.get(SubBandId=request.data['subband'])
            DateOfJoining=request.data["DateOfJoining"]
            FixedCTC=request.data["FixedCTC"]
            Isvariable = request.data["IsVariable"]
            VariablePay = request.data["VariablePay"]
            MQVariable=request.data["MQVariable"]
            Is_Eligible_annu_Mgnt_Bonus=request.data["Is_Eligible_annu_Mgnt_Bonus"]
            Is_Eligible_Joining_Bonus=request.data["Is_Eligible_Joining_Bonus"]
            IS_Eligible_Monthly_Incentive=request.data["IS_Eligible_Monthly_Incentive"]
            context = self.getContext(selectedcandidate, designation, band, subband, DateOfJoining,
                                    FixedCTC, Isvariable, VariablePay, MQVariable, Is_Eligible_annu_Mgnt_Bonus,
                                    Is_Eligible_Joining_Bonus, IS_Eligible_Monthly_Incentive)
            return Response(context,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
    
    def getContext(self,selectedcandidate, designation, band, subband, DateOfJoining,
                                  FixedCTC, Isvariable, VariablePay, MQVariable, Is_Eligible_annu_Mgnt_Bonus,
                                  Is_Eligible_Joining_Bonus, IS_Eligible_Monthly_Incentive):
        
        varDOJ = None
        varDate = None
        varDesignation = None
        varName =  None
        varLocation = None
        varBand = None
        varSubBand = None 
        varGMI = None
        varGPA = None
        iSMngtBonus = False
        iSVariablePay = False
        iSJoinBonus = False
        iSMonthIncentive = False
        varSalary = None
        varSalaryWords = None
        varTotalACTC = None
        varABasic = None
        varMBasic = None
        varAHRA = None
        varMHRA = None
        varAPF = None
        varMPF = None
        iSBonus  = False
        varABonus = None
        varMBonus = None
        iSShiftAllow   = False
        varAShiftAllow = None
        varMShiftAllow = None
        varAFBP   = None
        varMFBP = None
        varTotalMCTC = None

        businessunitname = None
        varTotalFixedCTC = None
        varVariablePay = None
        varFixedPayPerc = None
        varVariablePayPerc = None


     

        varDate = datetime.now()
        varDOJ = DateOfJoining
        if designation is not None:
            varDesignation = designation.DesignationName
        if selectedcandidate is not None: 
            varName =  selectedcandidate.candidate.CanLastName+', '+selectedcandidate.candidate.CanFirstName
            varLocation = selectedcandidate.candidate.Jobpost.Location.LocationName
            businessunitname = selectedcandidate.candidate.Jobpost.BusinessUnit.BusinessUnitName
        if  band is not None:
            varBand = band.BandName
            insurance = Insurance.objects.filter(BandId = band.BandId).first()
            if insurance is not None:                
                varGMI = round(insurance.InsuranceLimit)
                varGPA = round(insurance.AccidentLimit)
        if  subband is not None:
            varSubBand = subband.SubBandName
        iSMngtBonus = Is_Eligible_annu_Mgnt_Bonus
        iSVariablePay = Isvariable
        iSJoinBonus = Is_Eligible_Joining_Bonus
        iSMonthIncentive = IS_Eligible_Monthly_Incentive 

        varTotalFixedCTC = FixedCTC
        varTotalMCTC = round(varTotalFixedCTC/12)

        if Isvariable == True:
           varVariablePay = VariablePay
           varTotalACTC =  FixedCTC+VariablePay
           varFixedPayPerc = round((FixedCTC/(FixedCTC+VariablePay)) * 100)
           varVariablePayPerc = round((VariablePay/(FixedCTC+VariablePay)) * 100)
        elif Isvariable == False:
            varTotalACTC = FixedCTC

        if varTotalACTC is not None:
           varSalary = varTotalACTC
           varSalaryWords = self.num2words(varTotalACTC)
           

        if varTotalFixedCTC is not None:  
           varABasic = round(varTotalFixedCTC * 0.4)
           varMBasic = round(varABasic/12)

        if varMBasic is not None and varMBasic < 15000:
            varMBasic = 15000
            varABasic = round(varMBasic * 12)
        if varABasic is not None:
            varAHRA = round(varABasic * 0.4)
            varMHRA = round(varAHRA/12)
            varAPF = round(varABasic * 0.12)
            varMPF = round(varAPF/12)
        if varMBasic is not None and varMBasic <= 21000:  
            iSBonus = True
            varMBonus = 1400
            varABonus = round(varMBonus * 12)

        if businessunitname is not None and businessunitname == "Workforce Solutions":
            iSShiftAllow = True
            varMShiftAllow = 3000
            varAShiftAllow = round(varMShiftAllow * 12)
        if varTotalACTC is not None and varABasic is not None and varAHRA is not None and varAPF is not None:
            
            varAFBP = round(varTotalFixedCTC-(varABasic+varAHRA+varAPF))
        if iSBonus is True:
            varAFBP =   round(varAFBP-varABonus)
        if iSShiftAllow is True:
             varAFBP = round(varAFBP- varAShiftAllow)
        if varAFBP is not None:
            varMFBP = round(varAFBP/12)

        context = {
                    "varDate" :varDate,
                    "varName"  : varName,
                    "varDesignation" : varDesignation,
                    "varBand" : varBand,
                    "varSubBand" : varSubBand,
                    "varDOJ" : varDOJ,
                    "varSalary" : varSalary,
                    "varSalaryWords" : varSalaryWords,
                    "varLocation" : varLocation,
                    "varTotalFixedCTC" : varTotalFixedCTC,      
                    "varTotalACTC" : varTotalACTC,
                    "varTotalMCTC" : varTotalMCTC,
                    "varABasic" : varABasic,
                    "varMBasic" : varMBasic,
                    "varAHRA" : varAHRA,
                    "varMHRA" : varMHRA,
                    "varAPF" : varAPF,
                    "varMPF" : varMPF,
                    "iSBonus" : iSBonus,
                    "varABonus" : varABonus,
                    "varMBonus" : varMBonus,
                    "iSShiftAllow" : iSShiftAllow ,
                    "varAShiftAllow" : varAShiftAllow,
                    "varMShiftAllow" : varMShiftAllow,
                    "varAFBP" : varAFBP,
                    "varMFBP" : varMFBP,
                    "varGMI" : varGMI,
                    "varGPA" : varGPA,
                    "iSMngtBonus" : iSMngtBonus,                    
                    "iSJoinBonus" : iSJoinBonus ,
                    "iSMonthIncentive" : iSMonthIncentive,
                    "iSVariablePay" : iSVariablePay,
                    "varVariablePay": varVariablePay,
                    "varFixedPayPerc" : varFixedPayPerc,
                    "varVariablePayPerc" :varVariablePayPerc


                 }
        return  context 

    def num2words(self,num):
        num = decimal.Decimal(num)
        decimal_part = num - int(num)
        num = int(num)

        if decimal_part:
            return self.num2words(num) + " point " + (" ".join(self.num2words(i) for i in str(decimal_part)[2:]))

        under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        above_100 = {100: 'Hundred', 1000: 'Thousand', 100000: 'Lakhs', 10000000: 'Crores'}

        if num < 20:
            return under_20[num]

        if num < 100:
            return tens[num // 10 - 2] + ('' if num % 10 == 0 else ' ' + under_20[num % 10])

        # find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
        pivot = max([key for key in above_100.keys() if key <= num])

        return self.num2words(num // pivot) + ' ' + above_100[pivot] + ('' if num % pivot==0 else ' ' + self.num2words(num % pivot))
      