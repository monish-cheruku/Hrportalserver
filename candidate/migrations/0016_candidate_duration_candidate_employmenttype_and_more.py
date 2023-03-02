# Generated by Django 4.0.8 on 2023-02-21 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ManageLocation', '0004_alter_location_locationname'),
        ('candidate', '0015_remove_selected_candidates_candidatecategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='Duration',
            field=models.IntegerField(db_column='Duration', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='EmploymentType',
            field=models.CharField(db_column='Employment_Type', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='Location',
            field=models.ForeignKey(db_column='Location_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='ManageLocation.location'),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='Duration',
            field=models.IntegerField(db_column='Duration', null=True),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='EndDate',
            field=models.DateTimeField(blank=True, db_column='EndDate', null=True),
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='NoOfHours',
            field=models.IntegerField(null=True),
        ),
    ]