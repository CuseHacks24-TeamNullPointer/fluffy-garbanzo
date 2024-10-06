from django.contrib.gis.db import models

# Create your models here.

class Marker(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        return self.name

from django.db import models
class CsvimportWater(models.Model):
    col_1 = models.IntegerField(primary_key=True, blank=False, null=False, default=0)
    #   col_2 = models.(blank=True, null=True)
    ##col_3 = models.(blank=True, null=True)
    #col_4 = models.(blank=True, null=True)
    #col_5 = models.(blank=True, null=True)
    #col_6 = models.DecimalField(max_digits=1002, decimal_places=10, blank=True, null=True, default=0)
    #col_7 = models.DecimalField(max_digits=1001, decimal_places=10, blank=True, null=True, default=0)
    #col_8 = models.DecimalField(max_digits=1002, decimal_places=10, blank=True, null=True, default=0)
    #col_9 = models.DecimalField(max_digits=1002, decimal_places=10, blank=True, null=True, default=0)

class Meta:
    managed = False
    db_table = u'"csvimport_water"'
