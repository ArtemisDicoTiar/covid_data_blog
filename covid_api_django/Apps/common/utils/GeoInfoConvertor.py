import difflib
import logging

import country_converter as coco
import pycountry as pc
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
logging.getLogger('coco').setLevel(logging.WARNING)


# This code targets on ISO 3166-1 (country) and 3166-2 (sub-regions)

def get_continent_name(country_code: str):
    if country_code:
        return coco.convert(names=country_code, to='continent')

    return None


def get_country_short_name(iso_code: str):
    country = pc.countries.get(alpha_3=iso_code)
    return country.name


def get_country_official_name(iso_code: str):
    return pc.countries.get(alpha_3=iso_code).name


def get_country_normalised_iso3_code(unorganised_name: str):
    cruises = {
        'MS Zaandam': 'USA',  # Cruise currently located on USA
        'Diamond Princess': 'JPN',  # Cruise currently located on Japan
    }
    if unorganised_name in cruises.keys():
        return cruises[unorganised_name]

    return coco.convert(names=unorganised_name, to='ISO3')


def get_country_normalised_name(unorganised_name: str):
    cruises = {
        'MS Zaandam': 'USA',  # Cruise currently located on USA
        'Diamond Princess': 'JPN',  # Cruise currently located on Japan
    }
    if unorganised_name in cruises.keys():
        return cruises[unorganised_name]

    return pc.countries.get(alpha_3=coco.convert(names=unorganised_name, to='ISO3')).name


def convert_code_from_2_to_3(iso_code: str):
    return coco.convert(names=iso_code, to='ISO3')


def get_country_iso_information(iso_code: str):
    if len(iso_code) == 2:
        return pc.countries.get(alpha_2=iso_code)
    elif len(iso_code) == 3:
        return pc.countries.get(alpha_3=iso_code)
    else:
        raise ValueError("Wrong ISO Code")


def get_subdivision_iso_information(country_code, subdivision_name):
    if type(subdivision_name) == str:
        search_result = sorted(
            [sub
             for sub
             in pc.subdivisions.get(country_code=get_country_iso_information(iso_code=country_code).alpha_2)
             ],
            key=lambda x: difflib.SequenceMatcher(None, subdivision_name, x.name).ratio(),
            reverse=True
        )
        return search_result[0].code

    return None
