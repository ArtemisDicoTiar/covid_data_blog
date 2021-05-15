import typing
from dataclasses import dataclass
from datetime import datetime

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
# @dataclass
# class CSSE_Cases(models.Model):
#     CountryCode: str
#     ContinentName: str
#     SubdivisionCode: typing.Optional[str]
#     date: datetime.date
#     confirmed: float
#     deaths: float
#     recovered: float
#     removed: float
#     active: float
#
#
# @dataclass
# class CSSE_Cases_prediction(models.Model):
#     predicted: datetime.date
#     CountryCode: str
#     ContinentName: str
#     date: datetime.date
#     confirmed_prediction: float
#     deaths_prediction: float
#
#
# @dataclass
# class CSSE_Cases_prediction_accuracy(models.Model):
#     calculated: datetime.date
#     CountryCode: str
#     ContinentName: str
#     yesterday_accuracy: float
#     lastweek_accuracy: float
