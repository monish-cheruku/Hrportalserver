from django.db import models

# Create your models here.
class AvgCTC(models.Model):
    Id = models.AutoField(primary_key=True, db_column='ID')
    ServiceLineId = models.IntegerField(null=False, db_column='Service_Line_ID')
    ExperienceLevelId = models.IntegerField(null=False, db_column='Experience_Level_ID')
    AvgApprovedCTC = models.FloatField(null=False, db_column='Avg_Approved_CTC')
    AvgBillRate = models.FloatField(null=True, db_column='Avg_Bill_Rate')

    class Meta:    
        db_table = 'AvgCTC'