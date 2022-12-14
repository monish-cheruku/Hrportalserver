# Generated by Django 4.0.8 on 2022-12-29 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_alter_candidateapprovalmodel_approvalstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selected_Candidates',
            fields=[
                ('Selected_Candidate_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Is_Offer_Accepted', models.BooleanField(db_column='Is_Offer_Accepted', default=False)),
                ('Is_Joined', models.BooleanField(db_column='Is_Joined', default=False)),
                ('HRC_ID', models.CharField(db_column='HRC_ID', max_length=100, null=True)),
                ('Employee_ID', models.CharField(db_column='Employee_ID', max_length=100, null=True)),
                ('Candidate_ID', models.ForeignKey(db_column='Candidate_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.candidate')),
            ],
            options={
                'db_table': 'Selected_Candidates',
            },
        ),
    ]
