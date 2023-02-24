# Generated by Django 4.0.8 on 2023-02-21 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0015_remove_selected_candidates_candidatecategory_and_more'),
        ('selectedcandidate', '0004_rename_passport_candidatepersonalinfo_passportnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatepersonalinfo',
            name='AADHAR',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='CandidatePfDetails',
            fields=[
                ('Id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('PreviousCompanyUAN', models.CharField(db_column='Prev_Company_UAN', max_length=50)),
                ('PreviousMemberId', models.CharField(db_column='Prev_Mem_ID', max_length=50)),
                ('MemberNameAsPerAadhar', models.CharField(db_column='Member_Name_As_Per_Aadhar', max_length=50)),
                ('DoB', models.CharField(db_column='DateOfBirth', max_length=20, null=True)),
                ('DoJ', models.CharField(db_column='Expected_DoJ', max_length=20, null=True)),
                ('Gender', models.CharField(db_column='Gender', max_length=20, null=True)),
                ('FatherOrHusbandName', models.CharField(db_column='Father/Husband Name', max_length=100)),
                ('Relation', models.CharField(db_column='Relation', max_length=50)),
                ('MaritalStatus', models.CharField(db_column='Marital_status', max_length=20, null=True)),
                ('InternationalWorker', models.BooleanField(db_column='International_Worker', default=False)),
                ('MobileNumber', models.CharField(db_column='ContactNumber', max_length=20, null=True)),
                ('EmailId', models.CharField(db_column='Email', max_length=20, null=True)),
                ('Nationality', models.CharField(db_column='Nationality', max_length=100)),
                ('wages', models.CharField(db_column='Wages', max_length=50)),
                ('Qualification', models.CharField(db_column='Qualification', max_length=20, null=True)),
                ('CountryOfOrigin', models.CharField(db_column='Country_Of_Origin', max_length=100)),
                ('PassportNumber', models.CharField(db_column='PassportNumber', max_length=20, null=True)),
                ('PassportValidFrom', models.CharField(db_column='PassportValidFrom', max_length=20, null=True)),
                ('PassportValidTill', models.CharField(db_column='PassportValidTo', max_length=20, null=True)),
                ('PhysicalHadicap', models.BooleanField(db_column='Physical_Hadicap', default=False)),
                ('BankAccNum', models.CharField(db_column='Account_Number', max_length=20, null=True)),
                ('IFSC', models.CharField(db_column='IFSC_Code', max_length=20, null=True)),
                ('NameAsPerBank', models.CharField(db_column='Name_As_Per_Bank', max_length=100)),
                ('PAN', models.CharField(db_column='PAN', max_length=20, null=True)),
                ('NameAsPerPan', models.CharField(db_column='Name_As_Per_Pan', max_length=100)),
                ('Aadhar', models.ForeignKey(db_column='AADHAR', null=True, on_delete=django.db.models.deletion.CASCADE, to='selectedcandidate.candidatepersonalinfo')),
                ('selectedCandidateid', models.ForeignKey(db_column='Selected_Candidate_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.selected_candidates')),
            ],
            options={
                'db_table': 'Candidate_PF_Details',
            },
        ),
    ]
