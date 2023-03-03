# Generated by Django 4.0.8 on 2023-03-03 05:52

import candidate.models.candidatemodel
import candidate.models.selected_Candidates_Model
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ManageSubBand', '0002_alter_subband_subbandname'),
        ('jobpost', '0005_remove_jobpost_experiancelevel'),
        ('ManageLocation', '0004_alter_location_locationname'),
        ('ManageExperienceLevel', '0010_rename_max_experiencerange_experience_max_experience_and_more'),
        ('ManageBand', '0003_alter_band_banddesc_alter_band_bandname'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ManageDesignation', '0004_alter_designation_designationname'),
        ('managestages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateActionModel',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CandidateApprovalID', models.BigIntegerField(db_column='Candidate_Approval_ID')),
                ('RoleName', models.CharField(db_column='Role_Name', max_length=50)),
                ('CandidateId', models.BigIntegerField(db_column='Candidate_ID')),
                ('CandidateCode', models.CharField(db_column='Candidate_Code', max_length=100)),
                ('CanFirstName', models.CharField(db_column='Can_First_Name', max_length=100)),
                ('CanLastName', models.CharField(db_column='Can_Last_Name', max_length=100)),
                ('CandidateName', models.CharField(db_column='Can_Name', max_length=200)),
                ('ContactNo', models.CharField(db_column='Contact_No', max_length=10)),
                ('CurrentCTC', models.IntegerField(db_column='Current_CTC')),
                ('ExpectedCTC', models.IntegerField(db_column='Expected_CTC')),
                ('NegotiatedCTC', models.IntegerField(db_column='Negotiated_CTC')),
                ('Skills', models.CharField(db_column='Skills', max_length=500)),
                ('Resume', models.CharField(db_column='Can_Resume', max_length=10000)),
                ('CurrentOrganization', models.CharField(db_column='Current_Org', max_length=200)),
                ('CurrentJobLocation', models.CharField(db_column='Current_Job_Loc', max_length=100)),
                ('Email', models.CharField(db_column='Email', max_length=100)),
                ('ExpectedDOJ', models.DateField(db_column='Expected_DOJ')),
                ('OverallExpYear', models.IntegerField(db_column='Overall_Exp_Year', null=True)),
                ('OverallExpMonth', models.IntegerField(db_column='Overall_Exp_Month', null=True)),
                ('ReleventExpYear', models.IntegerField(db_column='Relevent_Exp_Year', null=True)),
                ('ReleventExpMonth', models.IntegerField(db_column='Relevent_Exp_Month', null=True)),
                ('CandidateReleventExp', models.CharField(db_column='CAN_Relevent_Exp', max_length=50)),
                ('CandidateOverallExp', models.CharField(db_column='CAN_Overall_Exp', max_length=50)),
                ('AvgApprovedCTC', models.IntegerField(db_column='Can_Avg_Approved_CTC')),
                ('AvgBillRate', models.IntegerField(db_column='Can_Avg_Bill_Rate')),
                ('JobPostID', models.BigIntegerField(db_column='Job_Post_ID')),
                ('JobCode', models.CharField(db_column='Job_Code', max_length=100)),
                ('UserName', models.CharField(db_column='User_Name', max_length=50)),
                ('HiringManager', models.CharField(db_column='Hiring_Manager', max_length=100)),
                ('ApproverName', models.CharField(db_column='Approver_Name', max_length=50)),
                ('ApproverDisplayName', models.CharField(db_column='Approver_Display_Name', max_length=100)),
                ('ApproverEmail', models.CharField(db_column='Approver_Email', max_length=100)),
                ('JobTitle', models.CharField(db_column='Job_Title', max_length=100)),
                ('JobDesc', models.CharField(db_column='Job_Desc', max_length=1000)),
                ('EmploymentType', models.CharField(db_column='Employment_Type', max_length=50)),
                ('Duration', models.IntegerField(db_column='Dureation')),
                ('NoOfPositions', models.IntegerField(db_column='No_Of_Positions')),
                ('Qualification', models.CharField(db_column='Qualification', max_length=50)),
                ('OnBoardingDate', models.DateField(db_column='OnBoarding_Date')),
                ('POReference', models.CharField(db_column='PO_Ref', max_length=50)),
                ('stage_name', models.CharField(db_column='Stage_Name', max_length=50)),
                ('StageDesc', models.CharField(db_column='Satge_Desc', max_length=100)),
                ('industry_name', models.CharField(db_column='Industry_Name', max_length=100)),
                ('company_name', models.CharField(db_column='Company_Name', max_length=50)),
                ('businessunit_name', models.CharField(db_column='Business_Unit_Name', max_length=50)),
                ('serviceline_name', models.CharField(db_column='Service_Line_Name', max_length=50)),
                ('customer_name', models.CharField(db_column='Customer_Name', max_length=50)),
                ('location_name', models.CharField(db_column='Location_Name', max_length=50)),
                ('DefAvgApprovedCTC', models.IntegerField(db_column='Avg_Approved_CTC')),
                ('DefAvgBillRate', models.IntegerField(db_column='Avg_Bill_Rate')),
                ('MinimumExperiance', models.IntegerField(db_column='Minimum_Experiance')),
                ('MaximumExperiance', models.IntegerField(db_column='Maximum_Experiance')),
                ('MaximumCTC', models.IntegerField(db_column='Maximum_CTC')),
                ('Location', models.IntegerField(db_column='Can_Location_ID')),
                ('CanJobLocation', models.CharField(db_column='Can_Location_Name', max_length=50)),
                ('CanEmploymentType', models.CharField(db_column='Can_Employment_Type', max_length=50)),
                ('CanDuration', models.IntegerField(db_column='Can_Duration')),
            ],
            options={
                'db_table': 'view_candidateaction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('CandidateId', models.AutoField(db_column='Candidate_ID', primary_key=True, serialize=False)),
                ('CandidateCode', models.CharField(db_column='Candidate_Code', max_length=20, unique=True)),
                ('HRUserName', models.CharField(db_column='HR_User_Name', max_length=20, null=True)),
                ('CanFirstName', models.CharField(db_column='Can_First_Name', max_length=50, null=True)),
                ('CanLastName', models.CharField(db_column='Can_Last_Name', max_length=50, null=True)),
                ('Qualification', models.CharField(db_column='High_Qualification', max_length=30, null=True)),
                ('OverallExpYear', models.IntegerField(db_column='Overall_Exp_Year', null=True)),
                ('OverallExpMonth', models.IntegerField(db_column='Overall_Exp_Month', null=True)),
                ('ReleventExpYear', models.IntegerField(db_column='Relevent_Exp_Year', null=True)),
                ('ReleventExpMonth', models.IntegerField(db_column='Relevent_Exp_Month', null=True)),
                ('CurrentCTC', models.IntegerField(db_column='Current_CTC', null=True)),
                ('ExpectedCTC', models.IntegerField(db_column='Expected_CTC', null=True)),
                ('NegotiatedCTC', models.IntegerField(db_column='Negotiated_CTC', null=True)),
                ('ExpectedDOJ', models.DateField(db_column='Expected_DOJ')),
                ('CurrentOrganization', models.CharField(db_column='Current_Org', max_length=50, null=True)),
                ('CurrentJobLocation', models.CharField(db_column='Current_Job_Loc', max_length=50, null=True)),
                ('Skills', models.CharField(db_column='Skills', max_length=200, null=True)),
                ('Email', models.CharField(db_column='Email', max_length=100, null=True)),
                ('ContactNo', models.CharField(db_column='Contact_No', max_length=20, null=True)),
                ('Resume', models.FileField(upload_to=candidate.models.candidatemodel.Candidate.get_upload_path)),
                ('AvgApprovedCTC', models.IntegerField(db_column='Avg_Approved_CTC', null=True)),
                ('AvgBillRate', models.IntegerField(db_column='Avg_Bill_Rate', null=True)),
                ('CreatedBy', models.CharField(db_column='Created_By', max_length=20, null=True)),
                ('CreatedOn', models.DateTimeField(blank=True, db_column='Created_On', null=True)),
                ('ModifiedBy', models.CharField(db_column='Modified_By', max_length=20, null=True)),
                ('ModifiedOn', models.DateTimeField(blank=True, db_column='Modified_On', null=True)),
                ('Comments', models.CharField(blank=True, db_column='Comments', max_length=500, null=True)),
                ('EmploymentType', models.CharField(db_column='Employment_Type', max_length=30, null=True)),
                ('Duration', models.IntegerField(db_column='Duration', null=True)),
                ('ExperianceLevel', models.ForeignKey(db_column='Experience_Level_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='ManageExperienceLevel.experience')),
                ('Jobpost', models.ForeignKey(db_column='Job_Post_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='jobpost.jobpost')),
                ('Location', models.ForeignKey(db_column='Location_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='ManageLocation.location')),
                ('Stage', models.ForeignKey(db_column='Stage_Id', null=True, on_delete=django.db.models.deletion.CASCADE, to='managestages.stage')),
            ],
            options={
                'db_table': 'HW_Candidate_Details',
            },
        ),
        migrations.CreateModel(
            name='candidatecategorymodel',
            fields=[
                ('candidatecategoryID', models.AutoField(db_column='candidatecategoryID', primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback_Category',
            fields=[
                ('FeedbackCategoryID', models.AutoField(db_column='Feedback_Category_ID', primary_key=True, serialize=False)),
                ('InterviewType', models.CharField(db_column='Interview_Type', max_length=40)),
                ('FeedbackCategory', models.CharField(db_column='Feedback_Category', max_length=60)),
                ('Stage', models.CharField(db_column='Stage_Name', default='', max_length=200)),
            ],
            options={
                'db_table': 'Feedback_Category',
            },
        ),
        migrations.CreateModel(
            name='Selected_Candidates',
            fields=[
                ('Selected_Candidate_ID', models.AutoField(primary_key=True, serialize=False)),
                ('IsOfferAccepted', models.BooleanField(db_column='Is_Offer_Accepted', default=False)),
                ('IsJoined', models.BooleanField(db_column='Is_Joined', default=False)),
                ('HRCID', models.CharField(db_column='HRC_ID', default=None, max_length=100, null=True)),
                ('EmployeeID', models.CharField(db_column='Employee_ID', default=None, max_length=100, null=True)),
                ('DateOfJoining', models.DateField(db_column='Date_Of_Joining', default=None, null=True)),
                ('FixedCTC', models.FloatField(db_column='Fixed_CTC', default=0)),
                ('IsVariable', models.BooleanField(db_column='Is_Variable', default=None, null=True)),
                ('VariablePerc', models.FloatField(db_column='Variable_Perc', default=0, null=True)),
                ('VariablePay', models.FloatField(db_column='Variable_Pay', default=0, null=True)),
                ('MQVariable', models.CharField(default=None, max_length=20, null=True)),
                ('FinalCTC', models.FloatField(db_column='Final_CTC', default=0)),
                ('ShiftAllowance', models.FloatField(db_column='Shift_Allowance', default=None, null=True)),
                ('Is_Eligible_annu_Mgnt_Bonus', models.BooleanField(db_column='IsEligibleannuMgntBonus', default=False)),
                ('Is_Eligible_Joining_Bonus', models.BooleanField(db_column='IsEligibleJoiningBonus', default=False)),
                ('JoiningBonus', models.FloatField(db_column='Joining_Bonus', default=None, null=True)),
                ('IS_Eligible_Monthly_Incentive', models.BooleanField(db_column='ISEligibleMonthlyIncentive', default=False)),
                ('OfferLetter', models.FileField(db_column='Offer_Letter', default=None, null=True, upload_to=candidate.models.selected_Candidates_Model.Selected_Candidates.get_upload_path)),
                ('Created_By', models.CharField(db_column='CreatedBy', default=None, max_length=50, null=True)),
                ('Created_on', models.DateField(db_column='Createdon', default=None, null=True)),
                ('Modified_By', models.CharField(db_column='ModifiedBy', default=None, max_length=50, null=True)),
                ('Modified_On', models.DateField(db_column='ModifiedOn', default=None, null=True)),
                ('VerificationStatus', models.CharField(db_column='Verification_Status', default=None, max_length=20, null=True)),
                ('VerificationComments', models.CharField(db_column='Verification_Comments', default=None, max_length=500, null=True)),
                ('BGVStatus', models.CharField(db_column='BGV_Status', default=None, max_length=20, null=True)),
                ('EndDate', models.DateTimeField(blank=True, db_column='EndDate', default=None, null=True)),
                ('NoOfHours', models.IntegerField(default=None, null=True)),
                ('Duration', models.IntegerField(db_column='Duration', default=None, null=True)),
                ('JoiningBonusLetter', models.FileField(db_column='JoiningBonus_Letter', default=None, null=True, upload_to=candidate.models.selected_Candidates_Model.Selected_Candidates.get_upload_path1)),
                ('band', models.ForeignKey(db_column='BandId', default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ManageBand.band')),
                ('candidate', models.ForeignKey(db_column='Candidate_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.candidate')),
                ('designation', models.ForeignKey(db_column='Designation_ID', default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ManageDesignation.designation')),
                ('subband', models.ForeignKey(db_column='SubBandId', default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ManageSubBand.subband')),
            ],
            options={
                'db_table': 'Selected_Candidates',
            },
        ),
        migrations.CreateModel(
            name='CandidateApprovalModel',
            fields=[
                ('CandidateApprovalId', models.AutoField(db_column='Candidate_Approval_ID', primary_key=True, serialize=False)),
                ('approverName', models.CharField(db_column='Approver_Name', max_length=20)),
                ('FirstName', models.CharField(db_column='First_Name', max_length=50)),
                ('LastName', models.CharField(db_column='Last_Name', max_length=50)),
                ('Email', models.CharField(db_column='Email', max_length=100)),
                ('approvalStatus', models.CharField(db_column='Approval_Status', max_length=40)),
                ('approvalDate', models.DateField(blank=True, db_column='Approval_Date', null=True)),
                ('approvalComments', models.CharField(db_column='Approval_Comments', max_length=1000, null=True)),
                ('CreatedOn', models.DateTimeField(blank=True, db_column='Created_On', null=True)),
                ('Candidate', models.ForeignKey(db_column='Candidate_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='candidate.candidate')),
                ('Stage', models.ForeignKey(db_column='Stage_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='managestages.stage')),
                ('role', models.ForeignKey(db_column='Role_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
            options={
                'db_table': 'HW_Candidate_Approval',
            },
        ),
        migrations.CreateModel(
            name='Candidate_Feedback',
            fields=[
                ('CandidateFeedbackID', models.AutoField(primary_key=True, serialize=False)),
                ('Comments', models.CharField(max_length=500, null=True)),
                ('Rating', models.IntegerField(null=True)),
                ('Candidate', models.ForeignKey(db_column='Candidate_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.candidate')),
                ('FeedbackCategory', models.ForeignKey(db_column='Feedback_Category_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.feedback_category')),
            ],
            options={
                'db_table': 'Candidate_Feedback',
            },
        ),
    ]
