from datetime import timedelta

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from route_decorator import Route

from Apps.CSSE.serializers import *
from Apps.CSSE.services import CSSEService
from Apps.common.utils.filter import prediction_parameter_validate
from Apps.common.utils.params import params

# Create your views here.

route = Route('/covid')


@route('/global', 'CSSE_cases')
class CSSE_CasesView(viewsets.ViewSet, ):
    csseService = CSSEService(filterRegion='country')

    schema = csseService.schema

    @action(methods=csseService.methods, detail=False)
    @params(CountryCode=str,
            startDate=str,
            offset=int)
    def cases(self, *args, **kwargs):
        CountryCode = kwargs['CountryCode']
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        queryset = CSSE_Cases.objects \
            .filter(CountryCode=CountryCode,
                    date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                 (datetime.strptime(startDate, '%Y-%m-%d')
                                  + timedelta(days=offset - 1)).date()
                                 )
                    )
        serializer_class = CSSE_CasesSerializer(queryset, many=True)

        return Response(self.csseService.get_linearised_data(serializer_class))

    @action(methods=csseService.methods, detail=False)
    @params(CountryCode=str,
            predictedDate=str,
            startDate=str,
            offset=int)
    def prediction(self, *args, **kwargs):
        CountryCode = kwargs['CountryCode']
        predictedDate = kwargs['predictedDate']
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        if prediction_parameter_validate(predictedDate=predictedDate, date=startDate, offset=offset):
            return prediction_parameter_validate(predictedDate=predictedDate, date=startDate, offset=offset)

        queryset = CSSE_Cases_prediction.objects \
            .filter(CountryCode=CountryCode,
                    predicted__exact=datetime.strptime(predictedDate, '%Y-%m-%d').date(),
                    date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                 (datetime.strptime(startDate, '%Y-%m-%d')
                                  + timedelta(days=offset - 1)).date()
                                 )
                    )
        serializer_class = CSSE_Cases_predictionSerializer(queryset, many=True)

        return Response(self.csseService.get_linearised_data(serializer_class))

    @action(methods=csseService.methods, detail=False)
    @params(CountryCode=str,
            startDate=str,
            offset=int)
    def predictionAccuracy(self, *args, **kwargs):
        CountryCode = kwargs['CountryCode']
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        queryset = CSSE_Cases_prediction_accuracy.objects \
            .filter(CountryCode=CountryCode,
                    calculated__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                       (datetime.strptime(startDate, '%Y-%m-%d')
                                        + timedelta(days=offset - 1)).date()
                                       )
                    )
        serializer_class = CSSE_Cases_prediction_accuracySerializer(queryset, many=True)

        return Response(self.csseService.get_linearised_data(serializer_class))
