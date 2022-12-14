# Generated by Django 4.0.7 on 2022-10-28 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('IndustryId', models.AutoField(db_column='Industry_ID', primary_key=True, serialize=False)),
                ('IndustryName', models.CharField(db_column='Industry_Name', max_length=100, null=True, unique=True)),
                ('IndustryDesc', models.CharField(db_column='Industry_Desc', max_length=500, null=True)),
                ('Active', models.BooleanField(db_column='Active', default=True, null=True)),
            ],
            options={
                'db_table': 'Industry',
            },
        ),
    ]
