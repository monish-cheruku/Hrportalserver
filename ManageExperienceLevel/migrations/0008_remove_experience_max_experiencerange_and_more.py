# Generated by Django 4.0.7 on 2022-10-27 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManageExperienceLevel', '0007_remove_experience_experiencerange_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='Max_ExperienceRange',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='Min_ExperienceRange',
        ),
    ]