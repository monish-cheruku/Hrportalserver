# Generated by Django 4.0.7 on 2023-02-27 15:22

from django.db import migrations, models
import django.db.models.deletion
import selectedcandidate.models.Candidatebankdetails
import selectedcandidate.models.Documentsupload


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidate', '0018_alter_selected_candidates_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidatePfDetails',
            fields=[
                ('Id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('PreviousCompanyUAN', models.CharField(db_column='Prev_Company_UAN', max_length=50)),
                ('PreviousMemberId', models.CharField(db_column='Prev_Mem_ID', max_length=50)),
                ('MemberNameAsPerAadhar', models.CharField(db_column='Member_Name_As_Per_Aadhar', max_length=50)),
                ('AADHAR', models.CharField(db_column='AADHAR', max_length=20, null=True)),
                ('DateOfBirth', models.CharField(db_column='DateOfBirth', max_length=20, null=True)),
                ('Date_Of_Joining', models.CharField(db_column='Date_Of_Joining', max_length=20, null=True)),
                ('Gender', models.CharField(db_column='Gender', max_length=20, null=True)),
                ('FatherOrHusbandName', models.CharField(db_column='Father/Husband Name', max_length=100)),
                ('Relation', models.CharField(db_column='Relation', max_length=50)),
                ('Marital_status', models.CharField(db_column='Marital_status', max_length=20, null=True)),
                ('InternationalWorker', models.BooleanField(db_column='International_Worker', default=False)),
                ('ContactNumber', models.CharField(db_column='ContactNumber', max_length=20, null=True)),
                ('Email', models.CharField(db_column='Email', max_length=20, null=True)),
                ('Nationality', models.CharField(db_column='Nationality', max_length=100)),
                ('wages', models.CharField(db_column='Wages', max_length=50)),
                ('Qualification', models.CharField(db_column='Qualification', max_length=20, null=True)),
                ('CountryOfOrigin', models.CharField(db_column='Country_Of_Origin', max_length=100)),
                ('PassportNumber', models.CharField(db_column='PassportNumber', max_length=20, null=True)),
                ('PassportValidFrom', models.CharField(db_column='PassportValidFrom', max_length=20, null=True)),
                ('PassportValidTill', models.CharField(db_column='PassportValidTo', max_length=20, null=True)),
                ('PhysicalHadicap', models.BooleanField(db_column='Physical_Hadicap', default=False)),
                ('AccountNumber', models.CharField(db_column='Account_Number', max_length=20, null=True)),
                ('IFSCcode', models.CharField(db_column='IFSC_Code', max_length=20, null=True)),
                ('NameAsPerBank', models.CharField(db_column='Name_As_Per_Bank', max_length=100)),
                ('PAN', models.CharField(db_column='PAN', max_length=20, null=True)),
                ('NameAsPerPan', models.CharField(db_column='Name_As_Per_Pan', max_length=100)),
                ('selectedcandidateid', models.ForeignKey(db_column='Selected_Candidate_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.selected_candidates')),
            ],
            options={
                'db_table': 'Candidate_PF_Details',
            },
        ),
        migrations.CreateModel(
            name='CandidatePersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('DateOfBirth', models.DateField(blank=True, null=True)),
                ('Marital_status', models.CharField(blank=True, max_length=40, null=True)),
                ('Gender', models.CharField(max_length=30, null=True)),
                ('BloodGroup', models.CharField(max_length=5, null=True)),
                ('PAN', models.CharField(max_length=10, null=True)),
                ('AADHAR', models.CharField(max_length=20, null=True, unique=True)),
                ('Email', models.CharField(max_length=20, null=True)),
                ('ContactNumber', models.CharField(max_length=15, null=True)),
                ('EmergencycontactName', models.CharField(max_length=40, null=True)),
                ('EmergencycontactRelation', models.CharField(max_length=20, null=True)),
                ('EmergencycontactNumber', models.CharField(max_length=20, null=True)),
                ('PassportNumber', models.CharField(max_length=20, null=True)),
                ('PassportValidFrom', models.DateField(null=True)),
                ('PassportValidTo', models.DateField(null=True)),
                ('Address', models.CharField(max_length=500, null=True)),
                ('selectedCandidateid', models.ForeignKey(db_column='Selected_Candidate_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.selected_candidates')),
            ],
            options={
                'db_table': 'CandidatePersonalInfo',
            },
        ),
        migrations.CreateModel(
            name='CandidateInsuranceDetails',
            fields=[
                ('Id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('Name', models.CharField(db_column='Name', max_length=50)),
                ('DateOfBirth', models.DateField(blank=True, db_column='DoB', null=True)),
                ('Relationship', models.CharField(db_column='Relationship', max_length=30, null=True)),
                ('Gender', models.CharField(db_column='Gender', max_length=15, null=True)),
                ('Selected_Candidate_ID', models.ForeignKey(db_column='Selected_Candidate_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.selected_candidates')),
            ],
            options={
                'db_table': 'CandidateInsuranceDetails',
            },
        ),
        migrations.CreateModel(
            name='CandidateFamilyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=40, null=True)),
                ('Date_Of_Birth', models.DateField(null=True)),
                ('Relationship_with_employee', models.CharField(max_length=20, null=True)),
                ('Contact_Number', models.CharField(max_length=15, null=True)),
                ('selectedCandidateId', models.ForeignKey(db_column='selectedCandidateId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.selected_candidates')),
            ],
            options={
                'db_table': 'CandidateFamilyDetails',
            },
        ),
        migrations.CreateModel(
            name='CandidateEmployementDetials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PreviousCompanyName', models.CharField(default='', max_length=40)),
                ('PreviousCompanyAddress', models.CharField(default='', max_length=200, null=True)),
                ('Start_Date', models.DateField(blank=True, null=True)),
                ('End_Date', models.DateField(blank=True, null=True)),
                ('Designationonjoining', models.CharField(max_length=20, null=True)),
                ('Designationonleaving', models.CharField(max_length=20, null=True)),
                ('selectedCandidateId', models.ForeignKey(db_column='selectedCandidateId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.selected_candidates')),
            ],
            options={
                'db_table': 'CandidateEmployementDetails',
            },
        ),
        migrations.CreateModel(
            name='CandidateEducationalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qualification', models.CharField(db_column='Qualification', max_length=15)),
                ('Specialization', models.CharField(db_column='Specialization', max_length=20, null=True)),
                ('Start_Date', models.DateField(blank=True, db_column='Start_Date', null=True)),
                ('End_Date', models.DateField(blank=True, db_column='End_Date', null=True)),
                ('Institute', models.CharField(db_column='Institute', max_length=70, null=True)),
                ('Percentage', models.CharField(db_column='Percentage', max_length=5, null=True)),
                ('selectedCandidateId', models.ForeignKey(db_column='selectedCandidateId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.selected_candidates')),
            ],
            options={
                'db_table': 'CandidateEducationalDetails',
            },
        ),
        migrations.CreateModel(
            name='CandidateDocumentsUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailtypeId', models.IntegerField(null=True)),
                ('detailtype', models.CharField(max_length=30)),
                ('file', models.FileField(db_column='documentpath', max_length=300, upload_to=selectedcandidate.models.Documentsupload.CandidateDocumentsUpload.get_upload_path)),
                ('verified', models.BooleanField(default=None, null=True)),
                ('verificationcomments', models.CharField(max_length=80, null=True)),
                ('selectedcandidate', models.ForeignKey(db_column='selectedCandidateId', on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.selected_candidates')),
            ],
            options={
                'db_table': 'CandidateDocuments',
            },
        ),
        migrations.CreateModel(
            name='CandidateBankDetails',
            fields=[
                ('Id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('BankName', models.CharField(db_column='Bank_Name', max_length=100)),
                ('AccountNumber', models.CharField(db_column='Account_Number', max_length=100)),
                ('BranchName', models.CharField(db_column='Branch_Name', max_length=100)),
                ('IFSCcode', models.CharField(db_column='IFSC_Code', max_length=100)),
                ('BankPassbook', models.FileField(db_column='Bank_Passbook', null=True, upload_to=selectedcandidate.models.Candidatebankdetails.CandidateBankDetails.get_upload_path)),
                ('selectedcandidateid', models.ForeignKey(db_column='selectedcandidateid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.selected_candidates')),
            ],
            options={
                'db_table': 'Candidate_Bank_Details',
            },
        ),
    ]
