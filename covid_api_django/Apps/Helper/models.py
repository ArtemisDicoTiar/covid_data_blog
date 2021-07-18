from django.db import models


# Create your models here.

class GlobalRegionMeta(models.Model):
    country_code = models.TextField(primary_key=True)
    country_name = models.TextField()
    continent = models.TextField()
    Lat = models.FloatField()
    Long = models.FloatField(db_column='Long')

    class Meta:
        app_label = 'covid_base'
        db_table = '_meta_data'


class RegionTimeZone(models.Model):
    CountryCode = models.TextField(primary_key=True)
    timezone = models.IntegerField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'region_time'
