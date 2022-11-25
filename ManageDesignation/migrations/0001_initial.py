# Generated by Django 4.0.7 on 2022-10-17 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('DesignationId', models.AutoField(db_column='Designation_ID', primary_key=True, serialize=False)),
                ('DesignationName', models.CharField(db_column='Designation_Name', max_length=100, null=True)),
                ('DesignationDesc', models.CharField(db_column='Designation_Desc', max_length=900, null=True)),
                ('Active', models.BooleanField(db_column='Active', default=True, null=True)),
            ],
            options={
                'db_table': 'Designation',
            },
        ),
    ]