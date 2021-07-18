from rest_framework import serializers

from Apps.Helper.models import RegionTimeZone


class RegionTimeZone_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RegionTimeZone
        fields = [
            'CountryCode',
            'timezone',
        ]
