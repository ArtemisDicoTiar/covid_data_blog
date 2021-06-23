from datetime import timedelta, datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from route_decorator import Route

from Apps.UK.serializers import *
from Apps.UK.services import UKService
from Apps.common.utils.filter import prediction_parameter_validate
from Apps.common.utils.params import params

# Create your views here.

route = Route('/covid')


@route('/uk', 'UK_cases')
class UK_CasesView(viewsets.ViewSet, ):
    UKService = UKService()

    schema = UKService.schema

    @action(methods=UKService.methods, detail=False)
    @params(regionCode=str,
            startDate=str,
            offset=int)
    def cases(self, *args, **kwargs):
        code = kwargs['regionCode']
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        queryset = UK_Cases.objects \
            .filter(code__exact=code,
                    date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                 (datetime.strptime(startDate, '%Y-%m-%d')
                                  + timedelta(days=offset - 1)).date()
                                 )
                    )
        serializer_class = UK_CasesSerializer(queryset, many=True)

        return Response(self.UKService.get_linearised_data(serializer_class))

    @action(methods=UKService.methods, detail=False)
    @params(regionCode=str,
            predictedDate=str,
            startDate=str,
            offset=int)
    def prediction(self, *args, **kwargs):
        code = kwargs['regionCode']
        predictedDate = kwargs['predictedDate']
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        if prediction_parameter_validate(predictedDate=predictedDate, date=startDate, offset=offset):
            return prediction_parameter_validate(predictedDate=predictedDate, date=startDate, offset=offset)

        queryset = UK_Cases_prediction.objects \
            .filter(code__exact=code,
                    predicted__exact=datetime.strptime(predictedDate, '%Y-%m-%d').date(),
                    date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                 (datetime.strptime(startDate, '%Y-%m-%d')
                                  + timedelta(days=offset - 1)).date()
                                 )
                    )
        serializer_class = UK_Cases_predictionSerializer(queryset, many=True)

        return Response(self.UKService.get_linearised_data(serializer_class))

    @action(methods=UKService.methods, detail=False)
    @params(regionCode=str,
            startDate=str,
            offset=int)
    def predictionAccuracy(self, *args, **kwargs):
        code = kwargs['regionCode']
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        queryset = UK_Cases_prediction_accuracy.objects \
            .filter(code__exact=code,
                    calculated__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                       (datetime.strptime(startDate, '%Y-%m-%d')
                                        + timedelta(days=offset - 1)).date()
                                       )
                    )
        serializer_class = UK_Cases_prediction_accuracySerializer(queryset, many=True)

        return Response(self.UKService.get_linearised_data(serializer_class))

