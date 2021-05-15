from datetime import date, datetime, timedelta

from Apps.CSSE.models import *
from Apps.common.services import Params, BaseService
from rest_framework.schemas import ManualSchema

from Apps.common.utils.GeoInfoConvertor import get_country_official_name


class CSSE_CaseService(BaseService):
    methods = ['get']
    params = [
        Params(name='regionType', dtype=str, required=True,
               location='query', description="region Type: country/continent"),
        Params(name='regionName', dtype=str, required=True,
               location='query', description="region name: either ContinentName or Country's ISO3 Code."),
        Params(name='startDate', dtype=str, required=True,
               location='query', description="Query start date (format: %Y-%m-%d)"),
        Params(name='offset', dtype=int, required=True,
               location='query', description="The number of dates from startDate."),
    ]

    def __init__(self):
        super().__init__()

    def get_queryset(self, *args, **kwargs):
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        if kwargs['regionType'] == 'country':
            return CSSE_Cases.objects \
                .filter(CountryCode=kwargs['regionName'],
                        date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                     (datetime.strptime(startDate, '%Y-%m-%d')
                                      + timedelta(days=offset - 1)).date()
                                     )
                        )
        elif kwargs['regionType'] == 'continent':
            return CSSE_Cases.objects \
                .filter(CountryCode=kwargs['regionName'],
                        date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                     (datetime.strptime(startDate, '%Y-%m-%d')
                                      + timedelta(days=offset - 1)).date()
                                     )
                        )

    @staticmethod
    def get_linearised_data(serialiser):
        return {
            'CountryCode': serialiser.data[0]['CountryCode'],
            'CountryName': get_country_official_name(serialiser.data[0]['CountryCode']),
            'ContinentName': serialiser.data[0]['ContinentName'],
            'date': [serialiser.data[row]['date'] for row in range(len(serialiser.data))],
            'confirmed': [serialiser.data[row]['confirmed'] for row in range(len(serialiser.data))],
            'deaths': [serialiser.data[row]['deaths'] for row in range(len(serialiser.data))],
            'recovered': [serialiser.data[row]['recovered'] for row in range(len(serialiser.data))],
            'removed': [serialiser.data[row]['removed'] for row in range(len(serialiser.data))],
        }


class CSSE_CasePredictionService(BaseService):
    methods = ['get']
    params = [
        Params(name='regionType', dtype=str, required=True,
               location='query', description="region Type: country/continent"),
        Params(name='regionName', dtype=str, required=True,
               location='query', description="region name: either ContinentName or Country's ISO3 Code."),
        Params(name='targetDate', dtype=str, required=True,
               location='query', description="Query prediction target date (format: %Y-%m-%d)"),
        Params(name='predictedOn(start)', dtype=str, required=True,
               location='query', description="Query for prediction start date (format: %Y-%m-%d)"),
        Params(name='offset', dtype=int, required=True,
               location='query', description="The number of dates from predictionStartDate."),
    ]

    def __init__(self):
        super().__init__()

    def get_queryset(self, *args, **kwargs):
        startDate = kwargs['predictedOn(start)']
        offset = kwargs['offset']

        if kwargs['regionType'] == 'country':
            return CSSE_Cases_prediction.objects \
                .filter(CountryCode=kwargs['regionName'],
                        predicted__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                          (datetime.strptime(startDate, '%Y-%m-%d')
                                           + timedelta(days=offset - 1)).date()),
                        date__exact=kwargs['targetDate'],
                        )
        elif kwargs['regionType'] == 'continent':
            return CSSE_Cases_prediction.objects \
                .filter(CountryCode=kwargs['regionName'],
                        predicted__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                          (datetime.strptime(startDate, '%Y-%m-%d')
                                           + timedelta(days=offset - 1)).date()),
                        date__exact=kwargs['targetDate'],
                        )

    @staticmethod
    def get_linearised_data(serialiser):
        return {
            'CountryCode': serialiser.data[0]['CountryCode'],
            'CountryName': get_country_official_name(serialiser.data[0]['CountryCode']),
            'ContinentName': serialiser.data[0]['ContinentName'],
            'targetDate': serialiser.data[0]['date'],
            'predictedOn': [serialiser.data[row]['predicted'] for row in range(len(serialiser.data))],
            'confirmed_prediction': [serialiser.data[row]['confirmed_prediction']
                                     for row in range(len(serialiser.data))],
            'deaths_prediction': [serialiser.data[row]['deaths_prediction']
                                  for row in range(len(serialiser.data))],
        }
