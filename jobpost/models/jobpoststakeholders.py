from django.db import models

class JobPostStakeHolders(models.Model):
    JobPostId = models.BigIntegerField(db_column='Job_Post_ID', primary_key=True)
    HMname = models.CharField(max_length=100, db_column='Hiring_Manager_Name')
    HMemail = models.CharField(max_length=100, db_column='Hiring_Manager_Email')
    BHname = models.CharField(max_length=100, db_column='Business_Head_Name')
    BHemail = models.CharField(max_length=100, db_column='Business_Head_Email')
    RecruiterName = models.CharField(max_length=100, db_column='Recruiter_Name')
    RecruiterEmail = models.CharField(max_length=100, db_column='Recruiter_Email')

    class Meta:   
        managed = False 
        db_table = 'view_jobpoststakeholders'






