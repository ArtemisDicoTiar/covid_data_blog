from datetime import date, datetime, timedelta

import coreapi
import coreschema
from django.shortcuts import render

# Create your views here.
from django.db.models import Count, Sum

from django_filters.rest_framework import DjangoFilterBackend

from django_rest_params.decorators import params
from drf_yasg.utils import swagger_auto_schema

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.schemas import AutoSchema, ManualSchema
from rest_framework.views import APIView
from route_decorator import Route

from Apps.CSSE.filter import prediction_parameter_validate
from Apps.CSSE.serializers import *
from Apps.CSSE.models import *
from route_decorator import Route

from Apps.CSSE.services import CSSEService, CSSESchema
from Apps.common.services import Params
from Apps.common.utils.schemaUtils import append_fields

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
