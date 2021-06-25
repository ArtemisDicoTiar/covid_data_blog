from django.db import models


# Create your models here.

class Google_Mobility(models.Model):
    CountryName = models.TextField()
    CountryCode = models.TextField(primary_key=True)
    date = models.DateField()

    retail_and_recreation_percent_change_from_baseline = models.FloatField()
    grocery_and_pharmacy_percent_change_from_baseline = models.FloatField()
    parks_percent_change_from_baseline = models.FloatField()
    transit_stations_percent_change_from_baseline = models.FloatField()
    workplaces_percent_change_from_baseline = models.FloatField()
    residential_percent_change_from_baseline = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'Google_Mobility'
