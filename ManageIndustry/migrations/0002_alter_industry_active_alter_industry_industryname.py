# Generated by Django 4.0.7 on 2022-10-30 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageIndustry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='Active',
            field=models.BooleanField(db_column='Active', default=True),
        ),
        migrations.AlterField(
            model_name='industry',
            name='IndustryName',
            field=models.CharField(db_column='Industry_Name', max_length=100, unique=True),
        ),
    ]
