# Generated by Django 4.0.7 on 2022-10-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageDesignation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='DesignationName',
            field=models.CharField(db_column='Designation_Name', max_length=100, null=True, unique=True),
        ),
    ]
