from rest_framework import serializers

from Apps.Google.models import Google_Mobility
from covid_info.models import *


class Google_MobilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Google_Mobility
        fields = [
            'CountryName',
            # 'CountryCode',
            'date',
            'retail_and_recreation_percent_change_from_baseline',
            'grocery_and_pharmacy_percent_change_from_baseline',
            'parks_percent_change_from_baseline',
            'transit_stations_percent_change_from_baseline',
            'workplaces_percent_change_from_baseline',
            'residential_percent_change_from_baseline',
        ]
