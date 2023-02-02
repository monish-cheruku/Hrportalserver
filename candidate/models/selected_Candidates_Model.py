import os
from django.db import models
from candidate.models.Feedback_Category_Model import Feedback_Category
from candidate.models.candidatemodel import Candidate
from ManageBand.models import Band
from ManageSubBand.models import SubBand
from candidate.models.CandidatecategoryModel import candidatecategorymodel
from ManageDesignation.models import Designation
class Selected_Candidates(models.Model):
    def get_upload_path(instance, filename):
        return os.path.join(str(instance.candidate.Jobpost.JobCode),str(instance.candidate.CandidateCode), 'OfferLetter',filename)     
    Selected_Candidate_ID=models.AutoField(primary_key=True)
    candidate=models.ForeignKey(Candidate,null=True,on_delete=models.DO_NOTHING,db_column="Candidate_ID")
    IsOfferAccepted=models.BooleanField(null=False,default=False,db_column="Is_Offer_Accepted")
    IsJoined=models.BooleanField(null=False,default=False,db_column="Is_Joined")
    HRCID=models.CharField(max_length=100,null=True,db_column="HRC_ID")
    EmployeeID=models.CharField(max_length=100,null=True,db_column="Employee_ID")  
    designation=models.ForeignKey(Designation,on_delete=models.DO_NOTHING,null=True,db_column="Designation_ID")
    subband=models.ForeignKey(SubBand,null=True,on_delete=models.DO_NOTHING,db_column="SubBandId")
    band=models.ForeignKey(Band,null=True,on_delete=models.DO_NOTHING,db_column="BandId")
    DateOfJoining=models.DateField(null=True,db_column="Date_Of_Joining")
    FixedCTC=models.IntegerField(db_column="Fixed_CTC",null=False,default=0)
    IsVariable=models.BooleanField(null=True,default=None,db_column="Is_Variable")
    VariablePay=models.IntegerField(null=True,db_column="Variable_Pay")
    MQVariable=models.CharField(null=True,max_length=20)
    FinalCTC=models.IntegerField(db_column="Final_CTC",null=False,default=0)
    candidatecategory=models.ForeignKey(candidatecategorymodel,null=True,on_delete=models.DO_NOTHING,db_column="candidate_category_ID")
    Is_Eligible_annu_Mgnt_Bonus=models.BooleanField(default=False,null=False,db_column="IsEligibleannuMgntBonus")
    Is_Eligible_Joining_Bonus=models.BooleanField(default=False,null=False,db_column="IsEligibleJoiningBonus")
    IS_Eligible_Monthly_Incentive=models.BooleanField(default=False,null=False,db_column="ISEligibleMonthlyIncentive")
    OfferLetter = models.FileField(upload_to=get_upload_path,null=True,db_column="Offer_Letter")
    Created_By=models.CharField(max_length=50,null=False,default="",db_column="CreatedBy")
    Created_on=models.DateField(db_column="Createdon",null=True)
    Modified_By=models.CharField(max_length=50,null=True,db_column="ModifiedBy")
    Modified_On=models.DateField(db_column="ModifiedOn",null=True)

    class Meta:  
        db_table="Selected_Candidates"