from datetime import date, datetime, timedelta

import coreapi
import coreschema
from django.shortcuts import render

# Create your views here.
from django.db.models import Count, Sum

from django_filters.rest_framework import DjangoFilterBackend

from django_rest_params.decorators import params

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.schemas import AutoSchema, ManualSchema
from rest_framework.views import APIView
from route_decorator import Route

from Apps.CSSE.serializers import *
from Apps.CSSE.models import *
from route_decorator import Route

from Apps.CSSE.services import CSSEService

route = Route('/covid')


@route('/global', 'CSSE_cases')
class CSSE_CasesView(viewsets.ViewSet, ):
    csseService = CSSEService(filterRegion='country')

    schema = csseService.schema

    @action(methods=csseService.methods, detail=False)
    @params(CountryCode=str,
            startDate=str,
            offset=int)
    # @CSSEService.param()
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

        return Response(self.get_linearised_data(serializer_class))

# class CSSE_CasesView(viewsets.ModelViewSet):
#     http_method_names = ['get']
#     # queryset = CSSE_Cases.objects.all()
#     serializer_class = CSSE_CasesSerializer
#
#     filterset_fields = {
#         'CountryCode': ['exact'],
#         'date': ['range', 'exact'],
#     }
#
# @action(methods=['get'], detail=True)
# @params(CountryCode=str,
#         startDate=str,
#         offset=int)
# def test_function(self, request, CountryCode, startDate, offset, *args, **kwargs):
#     queryset = COVID_Cases.objects \
#         .filter(CountryCode=CountryCode,
#                 date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
#                              (datetime.strptime(startDate, '%Y-%m-%d')
#                               + timedelta(days=offset-1)).date()
#                              )
#                 )
#     serializer_class = COVID_CasesSerializer(queryset, many=True)
#
#     return Response(
#         {
#             key: [
#                 serializer_class.data[row][key]
#                 for row in range(offset)
#             ]
#             for key in serializer_class.child.fields
#         }
#     )


# class CSSE_Cases_predictionView(viewsets.ModelViewSet):
#     http_method_names = ['get']
#     queryset = COVID_Cases_prediction.objects.all()
#     serializer_class = COVID_Cases_predictionSerializer
#
#     filterset_fields = {
#         'CountryCode': ['exact'],
#         'predicted': ['range', 'exact'],
#         'date': ['range', 'exact'],
#     }
#
#
# class CSSE_Cases_prediction_accuracyView(viewsets.ModelViewSet):
#     http_method_names = ['get']
#     queryset = COVID_Cases_prediction_accuracy.objects.all()
#     serializer_class = COVID_Cases_prediction_accuracySerializer
#
#     filterset_fields = {
#         'CountryCode': ['exact'],
#         'calculated': ['exact'],
#     }
