from rest_framework import serializers
from covid_info.models import *


class COVID_CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = COVID_Cases
        fields = [
            # 'CountryCode',
            # 'ContinentName',
            # 'SubdivisionCode',
            'date',
            'confirmed',
            'deaths',
            'recovered',
            'removed',
            'active',
        ]


class COVID_Cases_predictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = COVID_Cases_prediction
        fields = [
            'predicted',
            # 'CountryCode',
            # 'ContinentName',
            'date',
            'confirmed_prediction',
            'deaths_prediction',
        ]


class COVID_Cases_prediction_accuracySerializer(serializers.ModelSerializer):
    class Meta:
        model = COVID_Cases_prediction_accuracy
        fields = [
            'calculated',
            # 'CountryCode',
            # 'ContinentName',
            'yesterday_accuracy',
            'lastweek_accuracy',
        ]
