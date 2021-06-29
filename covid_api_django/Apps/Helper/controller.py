import json

import requests
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


def get_organised_region_info_from_long_lat(lat: float, long: float, key: str):
    def get_googleGeoInfo_from_long_lat(lat: float, long: float, key: str):
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&sensor=false".format(lat, long)
        v = requests.get(url, params={'key': key})
        j = json.loads(v.content)

        country = town = area_level_2 = None
        for c in j['results'][0]['address_components']:
            if "country" in c['types']:
                country = c['long_name']
            if "postal_town" in c['types']:
                town = c['long_name']
            if 'administrative_area_level_2' in c['types']:
                area_level_2 = c['long_name']
        return town, area_level_2, country

    town_name, province_name, country_name = get_googleGeoInfo_from_long_lat(lat, long, key)

    country_code = get_country_normalised_iso3_code(unorganised_name=country_name)
    continent_name = get_continent_name(country_code=country_code)
    res = {
        'continent': continent_name,
        'country': {'name': country_name, 'code': country_code},
    }

    if country_code == 'GBR':
        sub_regions = json.loads(
            requests.get('http://localhost:8000/api/region/uk/search/', params={'regionName': province_name}).content
        )
        if sub_regions:
            sub_region = sub_regions[0]
            res['sub_region'] = {'name': sub_region['name'], 'code': sub_region['code']}
        else:
            res['sub_region'] = None
    else:
        res['sub_region'] = (province_name, town_name)

    return Response(res)
