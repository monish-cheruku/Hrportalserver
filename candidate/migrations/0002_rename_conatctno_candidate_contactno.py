# Generated by Django 4.0.7 on 2022-12-03 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='ConatctNo',
            new_name='ContactNo',
        ),
    ]
