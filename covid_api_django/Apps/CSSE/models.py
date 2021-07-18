from django.db import models


# Create your models here.
class CSSE_Cases(models.Model):
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


class CSSE_Cases_prediction(models.Model):
    predicted = models.DateField()
    CountryCode = models.TextField(primary_key=True)
    ContinentName = models.TextField()
    date = models.DateField()
    confirmed_prediction = models.BigIntegerField()
    deaths_prediction = models.BigIntegerField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'COVID_Cases_prediction'


class CSSE_Cases_prediction_accuracy(models.Model):
    calculated = models.DateField()
    CountryCode = models.TextField(primary_key=True)
    ContinentName = models.TextField()
    yesterday_accuracy = models.FloatField()
    lastweek_accuracy = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'COVID_Cases_prediction_accuracy'


class CSSE_Cases_LSTM_prediction(models.Model):
    predicted = models.DateTimeField()
    CountryCode = models.TextField(primary_key=True)
    ContinentName = models.TextField()
    date = models.DateTimeField()
    confirmed_prediction = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'COVID_Cases_LSTM_prediction'


class CSSE_Cases_LSTM_prediction_accuracy(models.Model):
    calculated = models.DateField()
    CountryCode = models.TextField(primary_key=True)
    ContinentName = models.TextField()
    yesterday_accuracy = models.FloatField()
    lastweek_accuracy = models.FloatField()
    last2week_accuracy = models.FloatField()
    last4week_accuracy = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'COVID_Cases_LSTM_prediction_accuracy'
