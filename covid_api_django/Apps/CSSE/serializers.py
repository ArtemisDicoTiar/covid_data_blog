from rest_framework import serializers

from Apps.CSSE.models import *


class CSSE_CasesCountrySerializer(serializers.ModelSerializer):
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


class CSSE_CasesContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSSE_Cases
        fields = [
            'ContinentName',
            # 'SubdivisionCode',
            'date',
            'confirmed',
            'deaths',
            'recovered',
            'removed',
            'active',
        ]


class CSSE_Cases_predictionCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CSSE_Cases_prediction
        fields = [
            'predicted',

            # 'CountryCode',
          
            'ContinentName',
            'date',
            'confirmed_prediction',
            'deaths_prediction',
        ]


class CSSE_Cases_predictionContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSSE_Cases_prediction
        fields = [
            'predicted',
            'ContinentName',
            'date',
            'confirmed_prediction',
            'deaths_prediction',
        ]


class CSSE_Cases_prediction_accuracyCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CSSE_Cases_prediction_accuracy
        fields = [
            'calculated',
            'CountryCode',
            'ContinentName',
            'yesterday_accuracy',
            'lastweek_accuracy',
        ]


class CSSE_Cases_prediction_accuracyContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSSE_Cases_prediction_accuracy
        fields = [
            'calculated',
            'ContinentName',
            'yesterday_accuracy',
            'lastweek_accuracy',
        ]

