from django.db import models


# Create your models here.
class COVID_Cases(models.Model):
    CountryCode = models.TextField(primary_key=True)
    ContinentName = models.TextField()
    SubdivisionCode = models.TextField()
    date = models.DateField()
    confirmed = models.FloatField()
    deaths = models.FloatField()
    recovered = models.FloatField()
    removed = models.FloatField()
    active = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'COVID_Cases'


class COVID_Cases_prediction(models.Model):
    predicted = models.DateField()
    CountryCode = models.TextField(primary_key=True)
    ContinentName = models.TextField()
    date = models.DateField()
    confirmed_prediction = models.BigIntegerField()
    deaths_prediction = models.BigIntegerField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'COVID_Cases_prediction'


class COVID_Cases_prediction_accuracy(models.Model):
    calculated = models.DateField()
    CountryCode = models.TextField(primary_key=True)
    ContinentName = models.TextField()
    yesterday_accuracy = models.FloatField()
    lastweek_accuracy = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'COVID_Cases_prediction_accuracy'


class Google_Mobility(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'Google_Mobility'


class OWID_health(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_health'


class OWID_mortality(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_mortality'


class OWID_testing_data(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_testing_data'


class OWID_testing_meta(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_testing_meta'


class OWID_vaccination_data(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_vaccination_data'


class OWID_vaccination_meta(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'OWID_vaccination_meta'


class UK_Cases(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'UK_Cases'


class UK_Cases_prediction(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'UK_Cases_prediction'


class UK_Cases_prediction_accuracy(models.Model):
    class Meta:
        app_label = 'covid_info'
        db_table = 'UK_Cases_prediction_accuracy'
