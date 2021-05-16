from datetime import date, datetime, timedelta

from django.db.models import Sum, Count, Avg

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
                .values('CountryCode',
                        'ContinentName',
                        'date',
                        'confirmed',
                        'deaths',
                        'recovered',
                        'removed',
                        'active', ) \
                .filter(CountryCode=kwargs['regionName'],
                        date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                     (datetime.strptime(startDate, '%Y-%m-%d')
                                      + timedelta(days=offset - 1)).date()
                                     )
                        ).all()
        elif kwargs['regionType'] == 'continent':
            return CSSE_Cases.objects \
                .values('ContinentName', 'date') \
                .order_by('date') \
                .annotate(confirmed=Sum('confirmed'),
                          deaths=Sum('deaths'),
                          recovered=Sum('recovered'),
                          removed=Sum('removed'),
                          active=Sum('active')) \
                .filter(ContinentName=kwargs['regionName'].capitalize(),
                        date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                     (datetime.strptime(startDate, '%Y-%m-%d')
                                      + timedelta(days=offset - 1)).date()
                                     )
                        )

    @staticmethod
    def get_linearised_data(serialiser, *args, **kwargs):
        if not serialiser.data:
            return []

        base_res = {
            'ContinentName': serialiser.data[0]['ContinentName'],
            'date': [serialiser.data[row]['date'] for row in range(len(serialiser.data))],
            'confirmed': [serialiser.data[row]['confirmed'] for row in range(len(serialiser.data))],
            'deaths': [serialiser.data[row]['deaths'] for row in range(len(serialiser.data))],
            'recovered': [serialiser.data[row]['recovered'] for row in range(len(serialiser.data))],
            'removed': [serialiser.data[row]['removed'] for row in range(len(serialiser.data))],
            'active': [serialiser.data[row]['active'] for row in range(len(serialiser.data))],
        }
        if kwargs['regionType'] == 'country':
            base_res.update({
                'CountryCode': serialiser.data[0]['CountryCode'],
                'CountryName': get_country_official_name(serialiser.data[0]['CountryCode']),
            })

        return base_res


class CSSE_CasePredictionService(BaseService):
    methods = ['get']
    params = [
        Params(name='regionType', dtype=str, required=True,
               location='query', description="region Type: country/continent"),
        Params(name='regionName', dtype=str, required=True,
               location='query', description="region name: either ContinentName or Country's ISO3 Code."),
        Params(name='predictedOn', dtype=str, required=True,
               location='query', description="Query for predicted date (format: %Y-%m-%d)"),
        Params(name='targetDate', dtype=str, required=True,
               location='query', description="Query prediction target start date (format: %Y-%m-%d)"),
        Params(name='offset', dtype=int, required=True,
               location='query', description="The number of dates from targetDate."),
    ]

    def __init__(self):
        super().__init__()

    def get_queryset(self, *args, **kwargs):
        startDate = kwargs['targetDate']
        offset = kwargs['offset']

        if kwargs['regionType'] == 'country':
            return CSSE_Cases_prediction.objects \
                .values('predicted',
                        'CountryCode',
                        'ContinentName',
                        'date',
                        'confirmed_prediction',
                        'deaths_prediction', ) \
                .order_by('date') \
                .filter(CountryCode=kwargs['regionName'],
                        date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                     (datetime.strptime(startDate, '%Y-%m-%d')
                                      + timedelta(days=offset - 1)).date()),
                        predicted__exact=kwargs['predictedOn'],
                        )
        elif kwargs['regionType'] == 'continent':
            return CSSE_Cases_prediction.objects \
                .values('ContinentName', 'date', 'predicted') \
                .order_by('date') \
                .annotate(confirmed_prediction=Sum('confirmed_prediction'),
                          deaths_prediction=Sum('deaths_prediction')) \
                .filter(ContinentName=kwargs['regionName'].capitalize(),
                        date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                     (datetime.strptime(startDate, '%Y-%m-%d')
                                      + timedelta(days=offset - 1)).date()),
                        predicted__exact=kwargs['predictedOn'],
                        )

    @staticmethod
    def get_linearised_data(serialiser, *args, **kwargs):
        if not serialiser.data:
            return []

        base_res = {
            'ContinentName': serialiser.data[0]['ContinentName'],
            'predictedOn': serialiser.data[0]['predicted'],
            'targetDate': [serialiser.data[row]['date'] for row in range(len(serialiser.data))],
            'confirmed_prediction': [serialiser.data[row]['confirmed_prediction']
                                     for row in range(len(serialiser.data))],
            'deaths_prediction': [serialiser.data[row]['deaths_prediction']
                                  for row in range(len(serialiser.data))],
        }
        if kwargs['regionType'] == 'country':
            base_res.update({
                'CountryCode': serialiser.data[0]['CountryCode'],
                'CountryName': get_country_official_name(serialiser.data[0]['CountryCode']),
            })
        return base_res


class CSSE_CasePredictionAccuracyService(BaseService):
    methods = ['get']
    params = [
        Params(name='regionType', dtype=str, required=True,
               location='query', description="region Type: country/continent"),
        Params(name='regionName', dtype=str, required=True,
               location='query', description="region name: either ContinentName or Country's ISO3 Code."),
        Params(name='calculatedOn', dtype=str, required=True,
               location='query', description="Target date for calculating accuracy"),
    ]

    def __init__(self):
        super().__init__()

    def get_queryset(self, *args, **kwargs):
        startDate = kwargs['calculatedOn']

        if kwargs['regionType'] == 'country':
            return CSSE_Cases_prediction_accuracy.objects \
                .values('calculated',
                        'CountryCode',
                        'ContinentName',
                        'yesterday_accuracy',
                        'lastweek_accuracy',
                        ) \
                .filter(CountryCode=kwargs['regionName'],
                        calculated=startDate,
                        )
        elif kwargs['regionType'] == 'continent':
            return CSSE_Cases_prediction_accuracy.objects \
                .values('calculated',
                        'ContinentName',
                        ) \
                .annotate(yesterday_accuracy=Avg('yesterday_accuracy'),
                          lastweek_accuracy=Avg('lastweek_accuracy')) \
                .filter(ContinentName=kwargs['regionName'].capitalize(),
                        calculated=startDate,
                        )

    @staticmethod
    def get_linearised_data(serialiser, *args, **kwargs):
        base_res = {
            'ContinentName': serialiser.data[0]['ContinentName'],
            'targetDate': serialiser.data[0]['calculated'],
            'yesterday_accuracy': serialiser.data[0]['yesterday_accuracy'],
            'lastweek_accuracy': serialiser.data[0]['lastweek_accuracy'],
        }
        if kwargs['regionType'] == 'country':
            base_res.update({
                'CountryCode': serialiser.data[0]['CountryCode'],
                'CountryName': get_country_official_name(serialiser.data[0]['CountryCode']),
            })

        return base_res
