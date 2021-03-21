from rest_framework import serializers
from covid_global.models import *


class COVIDGlobalMetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COVIDGlobal_Meta
        fields = [
            'country_code',
            'country_name',
            'continent',
            'Lat',
            'Long',
        ]


class COVIDGlobalContinentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = COVIDGlobal_ActiveContinent
        # fields = []

