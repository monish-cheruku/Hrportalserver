# Generated by Django 4.0.7 on 2022-10-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('ExperienceLevelId', models.AutoField(db_column='Experience_Level_ID', primary_key=True, serialize=False)),
                ('ExperienceLevel', models.CharField(db_column='Experience_Level', max_length=100, null=True)),
                ('ExperienceRange', models.IntegerField(db_column='Experience_Range', null=True)),
                ('Active', models.BooleanField(db_column='Active', default=True, null=True)),
            ],
            options={
                'db_table': 'Experience',
            },
        ),
    ]
