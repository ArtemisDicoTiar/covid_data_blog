from django.http import HttpResponseBadRequest
from rest_framework.response import Response

from Apps.common.utils.GeoInfoConvertor import *
from pprint import pprint as pp


def get_continent_list():
    return Response(sorted(['Asia', 'America', 'Africa', 'Europe', 'Oceania']))


def get_region_search_result(search_region: str):
    search_results = get_search_result(search_region)
    res = list(map(lambda res: {
        'code': res.alpha_3,
        'continent': get_continent_name(res.alpha_3),
        'short_name': get_country_short_name(res.alpha_3),
        'official_name': get_country_official_name(res.alpha_3)
    },
                   search_results
                   ))

    return Response(res[0] if len(res) == 1 else res)

