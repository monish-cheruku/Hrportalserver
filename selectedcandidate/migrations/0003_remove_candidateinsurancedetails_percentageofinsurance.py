# Generated by Django 4.0.8 on 2023-02-20 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selectedcandidate', '0002_candidatebankdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateinsurancedetails',
            name='PercentageofInsurance',
        ),
    ]
