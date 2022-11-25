from datetime import datetime
from django.db import models
from ManageCustomer.models import Customer
from ManageExperienceLevel.models import Experience
from ManageLocation.models import Location
from managebusinessunit.models import BusinessUnit
from managecompany.models import Company
from manageserviceline.models import ServiceLine

from managestages.models import Stage

# Create your models here.
    

class JobPostActionModel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    JobPostApprovalID = models.BigIntegerField(db_column='Job_Post_Approval_ID')
    JobPostID = models.BigIntegerField(db_column='Job_Post_ID')
    JobCode = models.CharField(max_length=100, db_column='Job_Code')
    UserName = models.CharField(max_length=50, db_column='User_Name')
    HiringManager = models.CharField(max_length=100, db_column='Hiring_Manager')
    ApproverName = models.CharField(max_length=50, db_column='Approver_Name')
    ApproverDisplayName = models.CharField(max_length=100, db_column='Approver_Display_Name')
    ApproverEmail = models.CharField(max_length=100, db_column='Approver_Email')
    JobTitle =models.CharField(max_length=100, db_column='Job_Title')
    JobDesc =models.CharField(max_length=1000, db_column='Job_Desc')
    EmploymentType = models.CharField(max_length=50, db_column='Employment_Type')
    Duration = models.IntegerField(db_column='Dureation')
    NoOfPositions = models.IntegerField(db_column='No_Of_Positions')
    Qualification = models.CharField(max_length=50, db_column='Qualification')
    OnBoardingDate = models.DateField(db_column='OnBoarding_Date')
    POReference = models.CharField(max_length=50, db_column='PO_Ref')
    Stage = models.CharField(max_length=50, db_column='Stage_Name')
    StageDesc = models.CharField(max_length=100, db_column='Satge_Desc')
    Industry =  models.CharField(max_length=100, db_column='Industry_Name')
    Company = models.CharField(max_length=50, db_column='Company_Name')
    BusinessUnit = models.CharField(max_length=50, db_column='Business_Unit_Name')
    ServiceLine = models.CharField(max_length=50, db_column='Service_Line_Name')
    Customer = models.CharField(max_length=50, db_column='Customer_Name')
    Location = models.CharField(max_length=50, db_column='Location_Name')
    ExperianceLevel = models.CharField(max_length=50, db_column='Experience_Level')


    class Meta:   
        managed = False 
        db_table = 'view_jobpostaction'

                      