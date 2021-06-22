from datetime import date, datetime, timedelta

from django.shortcuts import render

# Create your views here.
from django.db.models import Count, Sum

from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from Apps.common.utils.params import params
from covid_info.serializers import *
from covid_info.models import *


class COVID_CasesView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVID_Cases.objects.all()
    serializer_class = COVID_CasesSerializer

    filterset_fields = {
        'CountryCode': ['exact'],
        'date': ['range', 'exact'],
    }

    @action(methods=['get'], detail=True)
    @params(CountryCode=str,
            startDate=str,
            offset=int)
    def test_function(self, request, CountryCode, startDate, offset, *args, **kwargs):
        queryset = COVID_Cases.objects \
            .filter(CountryCode=CountryCode,
                    date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                 (datetime.strptime(startDate, '%Y-%m-%d')
                                  + timedelta(days=offset-1)).date()
                                 )
                    )
        serializer_class = COVID_CasesSerializer(queryset, many=True)

        return Response(
            {
                key: [
                    serializer_class.data[row][key]
                    for row in range(offset)
                ]
                for key in serializer_class.child.fields
            }
        )



class COVID_Cases_predictionView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVID_Cases_prediction.objects.all()
    serializer_class = COVID_Cases_predictionSerializer

    filterset_fields = {
        'CountryCode': ['exact'],
        'predicted': ['range', 'exact'],
        'date': ['range', 'exact'],
    }


class COVID_Cases_prediction_accuracyView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVID_Cases_prediction_accuracy.objects.all()
    serializer_class = COVID_Cases_prediction_accuracySerializer

    filterset_fields = {
        'CountryCode': ['exact'],
        'calculated': ['exact'],
    }


class Google_MobilityView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Google_Mobility.objects.all()
    serializer_class = Google_MobilitySerializer

    filterset_fields = {
        'CountryCode': ['exact'],
        'date': ['range', 'exact'],
    }


class OWID_healthView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = OWID_health.objects.all()
    serializer_class = OWID_healthSerializer

    filterset_fields = {
        'iso_code': ['exact'],
        'date': ['range', 'exact'],
    }


class OWID_mortalityView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = OWID_mortality.objects.all()
    serializer_class = OWID_mortalitySerializer

    filterset_fields = {
        'iso_code': ['exact'],
        'date': ['exact', 'range'],
    }


class OWID_testing_dataView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVID_Cases_prediction_accuracy.objects.all()
    serializer_class = COVID_Cases_prediction_accuracySerializer

    filterset_fields = {
        # 'CountryCode': ['exact'],
        # 'calculated': ['exact'],
    }


class OWID_testing_metaView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVID_Cases_prediction_accuracy.objects.all()
    serializer_class = COVID_Cases_prediction_accuracySerializer

    filterset_fields = {
        # 'CountryCode': ['exact'],
        # 'calculated': ['exact'],
    }


class OWID_vaccination_dataView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVID_Cases_prediction_accuracy.objects.all()
    serializer_class = COVID_Cases_prediction_accuracySerializer

    filterset_fields = {
        # 'CountryCode': ['exact'],
        # 'calculated': ['exact'],
    }


class OWID_vaccination_metaView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVID_Cases_prediction_accuracy.objects.all()
    serializer_class = COVID_Cases_prediction_accuracySerializer

    filterset_fields = {
        # 'CountryCode': ['exact'],
        # 'calculated': ['exact'],
    }


class UK_CasesView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVID_Cases_prediction_accuracy.objects.all()
    serializer_class = COVID_Cases_prediction_accuracySerializer

    filterset_fields = {
        # 'CountryCode': ['exact'],
        # 'calculated': ['exact'],
    }


class UK_Cases_predictionView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVID_Cases_prediction_accuracy.objects.all()
    serializer_class = COVID_Cases_prediction_accuracySerializer

    filterset_fields = {
        # 'CountryCode': ['exact'],
        # 'calculated': ['exact'],
    }


class UK_Cases_prediction_accuracyView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVID_Cases_prediction_accuracy.objects.all()
    serializer_class = COVID_Cases_prediction_accuracySerializer

    filterset_fields = {
        # 'CountryCode': ['exact'],
        # 'calculated': ['exact'],
    }
