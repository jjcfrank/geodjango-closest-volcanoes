from django.contrib.gis.db import models

class Volcanoe(models.Model):
    name = models.CharField(max_length=75)
    location = models.PointField()
    elevation = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=50)