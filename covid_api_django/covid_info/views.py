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
