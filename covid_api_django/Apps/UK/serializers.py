from rest_framework import serializers

from Apps.UK.models import *


class UK_CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UK_Cases
        fields = [
            'date',

            'code',
            'name',
            'areaType',

            # 'maleCases',
            # 'femaleCases',

            # 'hospitalCases',
            # 'ventilatorBedOccupancy',
            # 'plannedCapacityByPublishDate',

            # 'testDaily',
            # 'testCumulative',

            'confirmedDaily',
            'confirmedCumulative',

            # 'deathsDaily',
            # 'deathsCumulative',

            # 'newDeaths28DaysByPublishDate',
            # 'cumDeaths28DaysByPublishDate',
            # 'cumDeaths28DaysByPublishDateRate',
            #
            # 'newDeaths28DaysByDeathDate',
            # 'cumDeaths28DaysByDeathDate',
            # 'cumDeaths28DaysByDeathDateRate',
        ]


class UK_Cases_predictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UK_Cases_prediction
        fields = [
            'predicted',
            'date',

            'code',
            'name',

            'confirmed_prediction',
            # 'deaths_prediction',
        ]


class UK_Cases_prediction_accuracySerializer(serializers.ModelSerializer):
    class Meta:
        model = UK_Cases_prediction_accuracy
        fields = [
            'calculated',

            'code',
            'name',

            'yesterday_accuracy',
            'lastweek_accuracy',
        ]
