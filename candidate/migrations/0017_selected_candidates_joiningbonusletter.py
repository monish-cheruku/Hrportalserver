# Generated by Django 4.0.7 on 2023-02-22 05:43

import candidate.models.selected_Candidates_Model
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0016_candidate_duration_candidate_employmenttype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='selected_candidates',
            name='JoiningBonusLetter',
            field=models.FileField(db_column='JoiningBonus_Letter', default=None, null=True, upload_to=candidate.models.selected_Candidates_Model.Selected_Candidates.get_upload_path1),
        ),
    ]