from rest_framework import serializers
from rest_framework_dataclasses.serializers import DataclassSerializer
from Apps.CSSE.models import *


class CSSE_CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSSE_Cases
        fields = [
            'CountryCode',
            'ContinentName',
            # 'SubdivisionCode',
            'date',
            'confirmed',
            'deaths',
            'recovered',
            'removed',
            'active',
        ]


class CSSE_Cases_predictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSSE_Cases_prediction
        fields = [
            'predicted',
            # 'CountryCode',
            # 'ContinentName',
            'date',
            'confirmed_prediction',
            'deaths_prediction',
        ]


class CSSE_Cases_prediction_accuracySerializer(serializers.ModelSerializer):
    class Meta:
        model = CSSE_Cases_prediction_accuracy
        fields = [
            'calculated',
            # 'CountryCode',
            # 'ContinentName',
            'yesterday_accuracy',
            'lastweek_accuracy',
        ]
