# Generated by Django 4.0.7 on 2022-12-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageAvgCTC', '0002_alter_avgctc_avgapprovedctc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='avgctc',
            name='BusinessUnitId',
            field=models.IntegerField(db_column='Business_Unit_ID'),
        ),
        migrations.AddField(
            model_name='avgctc',
            name='CompanyId',
            field=models.IntegerField(db_column='Company_ID'),
        ),
        migrations.AlterField(
            model_name='avgctc',
            name='AvgBillRate',
            field=models.FloatField(db_column='Avg_Bill_Rate'),
        ),
        migrations.AlterUniqueTogether(
            name='avgctc',
            unique_together={('CompanyId', 'BusinessUnitId', 'ServiceLineId', 'ExperienceLevelId')},
        ),
    ]
