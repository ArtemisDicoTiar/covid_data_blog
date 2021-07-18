from datetime import timedelta, datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from route_decorator import Route

import secrets_app
from Apps.Helper.controller import get_region_search_result, get_continent_list, get_organised_region_info_from_long_lat
from Apps.Helper.models import GlobalRegionMeta, RegionTimeZone
from Apps.Helper.serializers import RegionTimeZone_Serializer
from Apps.Helper.services import CountrySearch_Service, UKRegionSearch_Service, GeoApiSearch_Service
from Apps.UK.models import UK_Cases
from Apps.common.utils.params import params

route = Route('/region')


@route('/global', 'global_region_search')
class GlobalRegionSearch_View(viewsets.ViewSet, ):
    service = CountrySearch_Service()

    schema = service.schema

    @action(methods=service.methods, detail=False)
    @params(regionName=str)
    def search(self, *args, **kwargs):
        regionName = kwargs['regionName']

        return get_region_search_result(regionName)

    @action(methods=service.methods, detail=False)
    @params(CountryCode=str)
    def timezone(self, *args, **kwargs):
        CountryCode = kwargs['CountryCode']

        queryset = RegionTimeZone.objects.filter(CountryCode=str(CountryCode).capitalize())

        serializer_class = RegionTimeZone_Serializer(queryset, many=True)

        return self.service.get_linearised_data_from_serialiser(serializer_class)

    @action(methods=service.methods, detail=False)
    def continent_list(self, *args, **kwargs):
        return get_continent_list()

    @action(methods=service.methods, detail=False)
    @params(continent=str)
    def country_list(self, *args, **kwargs):
        continent = kwargs['continent']

        return self.service.get_linearised_data(GlobalRegionMeta.objects
                                                .filter(continent=str(continent).capitalize())
                                                .values('country_code', 'country_name')
                                                .distinct()
                                                .order_by('country_name')
                                                )


@route('/uk', 'uk_region_search')
class UKRegionSearch_View(viewsets.ViewSet, ):
    service = UKRegionSearch_Service()

    schema = service.schema

    @action(methods=service.methods, detail=False)
    @params(regionName=str)
    def search(self, *args, **kwargs):
        regionName = kwargs['regionName']

        return self.service.get_raw_linearised_data(query=UK_Cases.objects.raw(
            "SELECT DISTINCT name, code FROM covid_info.UK_Cases "
            "WHERE MATCH(name) AGAINST('{}')".format(regionName)
        ))

    @action(methods=service.methods, detail=False)
    def region_list(self, *args, **kwargs):
        return self.service.get_linearised_data(query=UK_Cases.objects
                                                .values('code', 'name')
                                                .distinct()
                                                .order_by('name')
                                                )


@route('/geoapi', 'googleGeoApi')
class GeoApiSearch_View(viewsets.ViewSet, ):
    service = GeoApiSearch_Service()

    schema = service.schema

    @action(methods=service.methods, detail=False)
    @params(long=float,
            lat=float,
            # key=str
            )
    def search(self, *args, **kwargs):
        lat = kwargs['lat']
        long = kwargs['long']
        key = secrets_app.GOOGLE_GEO_API_KEY

        return get_organised_region_info_from_long_lat(lat, long, key)

