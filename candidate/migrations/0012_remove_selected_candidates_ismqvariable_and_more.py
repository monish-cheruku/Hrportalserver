# Generated by Django 4.0.8 on 2023-01-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0011_alter_selected_candidates_band_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selected_candidates',
            name='IsMQVariable',
        ),
        migrations.AddField(
            model_name='selected_candidates',
            name='MQVariable',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
