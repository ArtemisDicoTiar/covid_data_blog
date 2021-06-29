import coreapi
from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from Apps.common.services import Params, BaseService
from Apps.common.utils.GeoInfoConvertor import get_country_official_name, get_country_short_name


class CountrySearch_Service(BaseService):
    def __init__(self):
        self.dropped_keys = []
        self.single_keys = []

        self.params = []
        self.methods = ['get']

        super(CountrySearch_Service, self).__init__(params=self.params, methods=self.methods,
                                                    dropped_keys=self.dropped_keys, single_keys=self.single_keys)
        self.schema = RegionSearch_Schema(self.fields)

    def get_linearised_data(self, query):
        if len(query) == 0:
            return HttpResponseBadRequest("Requested Data not found")

        return Response(list(map(lambda row: {'name': row['country_name'], 'code': row['country_code']}, query)))


class UKRegionSearch_Service(BaseService):
    def __init__(self):
        self.dropped_keys = []
        self.single_keys = []

        self.params = [
            Params(name='UKRegionName', dtype=str, required=True,
                   location='query', description="searching UK region code by its region name"),
        ]
        self.methods = ['get']

        super(UKRegionSearch_Service, self).__init__(params=self.params, methods=self.methods,
                                                     dropped_keys=self.dropped_keys, single_keys=self.single_keys)
        self.schema = RegionSearch_Schema(self.fields)

    def get_linearised_data(self, query):
        if len(query) == 0:
            return HttpResponseBadRequest("Requested Data not found")

        return Response(list(map(lambda row: {'name': row['name'], 'code': row['code']}, query)))

    @staticmethod
    def get_raw_linearised_data(query):
        if len(query) == 0:
            return HttpResponseBadRequest("Requested Data not found")

        return Response(list(map(lambda row: {'name': row.name, 'code': row.code}, query)))


class GeoApiSearch_Service(BaseService):
    def __init__(self):
        self.dropped_keys = []
        self.single_keys = []

        self.params = [
            Params(name='lat', dtype=float, required=True,
                   location='query', description="latitude"),
            Params(name='long', dtype=float, required=True,
                   location='query', description="longitude"),
            # Params(name='key', dtype=str, required=True,
            #        location='query', description="Google GeoCoding api key"),
        ]
        self.methods = ['get']

        super(GeoApiSearch_Service, self).__init__(params=self.params, methods=self.methods,
                                                   dropped_keys=self.dropped_keys, single_keys=self.single_keys)
        self.schema = RegionSearch_Schema(self.fields)


class RegionSearch_Schema(AutoSchema):
    manual_fields = []  # common fields

    def __init__(self, fields):
        super().__init__()
        self.manual_fields = fields

    def get_manual_fields(self, path, method):
        super().get_manual_fields(path, method)
        custom_fields = []
        if path.lower() in ["/api/region/global/continent_list/", "/api/region/uk/region_list/"]:
            self.manual_fields = []

        elif path.lower() == "/api/region/global/search/":
            self.manual_fields = []
            param = Params(name='regionName', dtype=str, required=True,
                           location='query', description="searching country ISO3 code by region name")

            custom_fields.append(
                coreapi.Field(
                    name=param.name,
                    required=param.required,
                    location=param.location,
                    schema=param.get_schema(),
                ),
            )

        elif path.lower() == "/api/region/global/country_list/":
            self.manual_fields = []
            continent = Params(name='continent', dtype=str, required=True,
                               location='query', description="continent name")
            custom_fields.append(
                coreapi.Field(
                    name=continent.name,
                    required=continent.required,
                    location=continent.location,
                    schema=continent.get_schema(),
                ),
            )

        elif path.lower() == "/api/region/uk/search/":
            self.manual_fields = []
            regionName = Params(name='regionName', dtype=str, required=True,
                                location='query', description="uk region name")
            custom_fields.append(
                coreapi.Field(
                    name=regionName.name,
                    required=regionName.required,
                    location=regionName.location,
                    schema=regionName.get_schema(),
                ),
            )

        return self.manual_fields + custom_fields
