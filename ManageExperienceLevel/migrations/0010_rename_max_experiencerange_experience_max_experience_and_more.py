# Generated by Django 4.0.7 on 2022-10-28 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageExperienceLevel', '0009_experience_max_experiencerange_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='Max_ExperienceRange',
            new_name='Max_Experience',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='Min_ExperienceRange',
            new_name='Min_Experience',
        ),
    ]
