from django.db import models


# Create your models here.
class UK_Cases(models.Model):
    date = models.DateField()

    code = models.TextField(primary_key=True)
    name = models.TextField()
    areaType = models.TextField()

    maleCases = models.TextField()
    femaleCases = models.TextField()

    hospitalCases = models.TextField()
    ventilatorBedOccupancy = models.TextField()
    plannedCapacityByPublishDate = models.TextField()

    testDaily = models.TextField()
    testCumulative = models.TextField()

    confirmedDaily = models.FloatField()
    confirmedCumulative = models.FloatField()

    deathsDaily = models.FloatField()
    deathsCumulative = models.FloatField()

    newDeaths28DaysByPublishDate = models.FloatField()
    cumDeaths28DaysByPublishDate = models.FloatField()
    cumDeaths28DaysByPublishDateRate = models.FloatField()

    newDeaths28DaysByDeathDate = models.FloatField()
    cumDeaths28DaysByDeathDate = models.FloatField()
    cumDeaths28DaysByDeathDateRate = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'UK_Cases'


class UK_Cases_prediction(models.Model):
    predicted = models.DateField()
    date = models.DateField()

    code = models.TextField(primary_key=True)
    name = models.TextField()

    confirmed_prediction = models.BigIntegerField()
    deaths_prediction = models.BigIntegerField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'UK_Cases_prediction'


class UK_Cases_prediction_accuracy(models.Model):
    calculated = models.DateField()

    code = models.TextField(primary_key=True)
    name = models.TextField()

    yesterday_accuracy = models.FloatField()
    lastweek_accuracy = models.FloatField()

    class Meta:
        app_label = 'covid_info'
        db_table = 'UK_Cases_prediction_accuracy'

