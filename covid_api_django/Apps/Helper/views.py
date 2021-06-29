from datetime import timedelta, datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from route_decorator import Route

from Apps.Helper.controller import get_region_search_result, get_continent_list
from Apps.Helper.models import GlobalRegionMeta
from Apps.Helper.services import CountrySearch_Service, UKRegionSearch_Service
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

        return self.service.get_linearised_data(query=UK_Cases.objects
                                                .filter(name__contains=str(regionName).capitalize())
                                                .values('code', 'name')
                                                .distinct()
                                                .order_by('name')
                                                )

    @action(methods=service.methods, detail=False)
    def region_list(self, *args, **kwargs):
        return self.service.get_linearised_data(query=UK_Cases.objects
                                                .values('code', 'name')
                                                .distinct()
                                                .order_by('name')
                                                )
