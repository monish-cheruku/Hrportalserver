# Generated by Django 4.0.8 on 2023-01-04 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ManageSubBand', '0002_alter_subband_subbandname'),
        ('ManageDesignation', '0004_alter_designation_designationname'),
        ('ManageBand', '0003_alter_band_banddesc_alter_band_bandname'),
        ('candidate', '0008_remove_selected_candidates_candidate_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='candidatecategorymodel',
            fields=[
                ('candidatecategoryID', models.AutoField(db_column='candidatecategoryID', primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='selected_candidates',
            old_name='Employee_ID',
            new_name='EmployeeID',
        ),
        migrations.RenameField(
            model_name='selected_candidates',
            old_name='HRC_ID',
            new_name='HRCID',
        ),
        migrations.RenameField(
            model_name='selected_candidates',
            old_name='Is_Joined',
            new_name='IsJoined',
        ),
        migrations.RenameField(
            model_name='selected_candidates',
            old_name='Is_Offer_Accepted',
            new_name='IsOfferAccepted',
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='Created_By',
            field=models.CharField(db_column='CreatedBy', default='', max_length=50),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='Created_on',
            field=models.DateField(db_column='Createdon', null=True),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='DateOfJoining',
            field=models.DateField(db_column='Date_Of_Joining', null=True),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='FinalCTC',
            field=models.IntegerField(db_column='Final_CTC', default=0),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='FixedCTC',
            field=models.IntegerField(db_column='Fixed_CTC', default=0),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='IS_Eligible_Monthly_Incentive',
            field=models.BooleanField(db_column='ISEligibleMonthlyIncentive', default=False),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='IsMQVariable',
            field=models.CharField(default='N', max_length=20),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='Is_Eligible_Joining_Bonus',
            field=models.BooleanField(db_column='IsEligibleJoiningBonus', default=False),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='Is_Eligible_annu_Mgnt_Bonus',
            field=models.BooleanField(db_column='IsEligibleannuMgntBonus', default=False),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='Modified_By',
            field=models.CharField(db_column='ModifiedBy', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='Modified_On',
            field=models.DateField(db_column='ModifiedOn', null=True),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='VariablePercentage',
            field=models.IntegerField(db_column='Variable_Percentage', null=True),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='band',
            field=models.ForeignKey(db_column='BandId', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='ManageBand.band'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='designation',
            field=models.ForeignKey(db_column='Designation_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ManageDesignation.designation'),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='subband',
            field=models.ForeignKey(db_column='SubBandId', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='ManageSubBand.subband'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='candidatecategory',
            field=models.ForeignKey(db_column='candidate_category_ID', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.candidatecategorymodel'),
            preserve_default=False,
        ),
    ]
