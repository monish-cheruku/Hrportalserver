# Generated by Django 4.0.7 on 2022-12-14 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0002_jobpost_maximumctc_jobpost_maximumexperiance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='maximumctc',
            new_name='MaximumCTC',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='maximumexperiance',
            new_name='MaximumExperiance',
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='minimumexperiance',
            new_name='MinimumExperiance',
        ),
    ]
