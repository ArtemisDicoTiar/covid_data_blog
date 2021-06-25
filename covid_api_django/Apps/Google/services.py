from datetime import date, datetime, timedelta

import coreapi
from django.db.models import Sum, Count, Avg

from Apps.CSSE.models import *
from Apps.common.services import Params, BaseService
from rest_framework.schemas import ManualSchema, AutoSchema

from Apps.common.utils.GeoInfoConvertor import get_country_official_name


class GoogleMobility_Service(BaseService):
    def __init__(self):
        self.params = [
            Params(name='regionCode', dtype=str, required=True,
                   location='query', description="Country code (ISO3)"),
            Params(name='startDate', dtype=str, required=True,
                   location='query', description="Query start date (format: %Y-%m-%d)"),
            Params(name='offset', dtype=int, required=True,
                   location='query', description="The number of dates from startDate."),

            # Params(name='retail_and_recreation', dtype=bool, required=True,
            #        location='header', description="requesting retail and recreation data"),
            # Params(name='grocery_and_pharmacy', dtype=bool, required=True,
            #        location='header', description="requesting grocery and pharmacy data"),
            # Params(name='parks', dtype=bool, required=True,
            #        location='header', description="requesting parks data"),
            # Params(name='transit_stations', dtype=bool, required=True,
            #        location='header', description="requesting transit stations data"),
            # Params(name='workplaces', dtype=bool, required=True,
            #        location='header', description="requesting workplaces data"),
            # Params(name='residential', dtype=bool, required=True,
            #        location='header', description="requesting residential data"),
        ]
        self.methods = ['get']

        super(GoogleMobility_Service, self).__init__(params=self.params, methods=self.methods)
        self.schema = GoogleMobility_Schema(self.fields)

    @staticmethod
    def get_linearised_data(serialiser):
        dropped_keys = []
        single_keys = ['CountryName', 'CountryCode']
        return dict(
            map(lambda key: (
                (key, map(lambda row_data: row_data[key], serialiser.data))
                if key not in dropped_keys and key not in single_keys
                else (
                    (key, serialiser.data[0][key])
                    if key in single_keys
                    else None
                )
            ),
                serialiser.child.fields)
        )


class GoogleMobility_Schema(AutoSchema):
    manual_fields = []  # common fields

    def __init__(self, fields):
        super().__init__()
        self.manual_fields = fields

    def get_manual_fields(self, path, method):
        super().get_manual_fields(path, method)
        custom_fields = []

        return self.manual_fields + custom_fields
