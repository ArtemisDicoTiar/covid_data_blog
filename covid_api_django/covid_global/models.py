from django.db import models
from conf import database


# Create your models here.

class COVIDGlobal_Meta(models.Model):
    country_code = models.CharField(primary_key=True)
    country_name = models.CharField()
    continent = models.CharField()
    Lat = models.FloatField()
    Long = models.FloatField()

    class Meta:
        managed = False
        app_label = 'covid_global_cumulative'
        db_table = '_meta_data'


class COVIDGlobal_ActiveContinent(models.Model):
    class Meta:
        managed = False
        app_label = 'covid_global_cumulative',
        db_table = 'active_continent'


class COVIDGlobal_ActiveCountry(models.Model):
    class Meta:
        managed = False
        app_label = 'covid_global_cumulative',


class COVIDGlobal_ConfirmedContinent(models.Model):
    class Meta:
        managed = False
        app_label = 'covid_global_cumulative',


class COVIDGlobal_ConfirmedCountry(models.Model):
    class Meta:
        managed = False
        app_label = 'covid_global_cumulative',


class COVIDGlobal_DeathsContinent(models.Model):
    class Meta:
        managed = False
        app_label = 'covid_global_cumulative',


class COVIDGlobal_DeathsCountry(models.Model):
    class Meta:
        managed = False
        app_label = 'covid_global_cumulative',


class COVIDGlobal_RecoveredContinent(models.Model):
    class Meta:
        managed = False
        app_label = 'covid_global_cumulative',


class COVIDGlobal_RecoveredCountry(models.Model):
    class Meta:
        managed = False
        app_label = 'covid_global_cumulative',


class COVIDGlobal_RemovedContinent(models.Model):
    class Meta:
        managed = False
        app_label = 'covid_global_cumulative',


class COVIDGlobal_RemovedCountry(models.Model):
    class Meta:
        managed = False
        app_label = 'covid_global_cumulative',
