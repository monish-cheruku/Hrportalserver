# Generated by Django 4.0.7 on 2022-10-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managecompany', '0002_alter_company_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='CompanyName',
            field=models.CharField(db_column='Company_Name', max_length=50, unique=True),
        ),
        migrations.AlterModelTable(
            name='company',
            table='Company',
        ),
    ]