from django.db import models
from candidate.models.selected_Candidates_Model import Selected_Candidates
import os

class CandidateInsuranceDetials(models.Model):
    
    Selected_Candidate_ID=models.ForeignKey(Selected_Candidates,null=True,on_delete=models.DO_NOTHING,db_column="Selected_Candidate_ID")
    Name=models.CharField(max_length=40,null=False)
    DateOfBirth=models.DateField(null=True,blank=True)
    Relationship=models.CharField(null=True,max_length=10)
    Gender=models.CharField(max_length=5,null=True)
    PercentageofInsurance=models.IntegerField(null=True,default=100)
    
    
    class Meta:
        db_table="CandidateInsuranceDetails"


