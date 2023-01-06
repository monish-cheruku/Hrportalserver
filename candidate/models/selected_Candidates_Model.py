from django.db import models
from candidate.models.Feedback_Category_Model import Feedback_Category
from candidate.models.candidatemodel import Candidate


class Selected_Candidates(models.Model):
    Selected_Candidate_ID=models.AutoField(primary_key=True)
    candidate=models.ForeignKey(Candidate,null=True,on_delete=models.DO_NOTHING,db_column="Candidate_ID")
    Is_Offer_Accepted=models.BooleanField(null=False,default=False,db_column="Is_Offer_Accepted")
    Is_Joined=models.BooleanField(null=False,default=False,db_column="Is_Joined")
    HRC_ID=models.CharField(max_length=100,null=True,db_column="HRC_ID")
    Employee_ID=models.CharField(max_length=100,null=True,db_column="Employee_ID")  
    class Meta:  
        db_table="Selected_Candidates"