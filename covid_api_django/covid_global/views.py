from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from covid_global.models import *
from covid_global.serializers import *


class COVIDGlobalMetaView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVIDGlobal_Meta.objects.all()
    serializer_class = COVIDGlobalMetaSerializer


class COVIDGlobal_ActiveContinentView(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = COVIDGlobal_ActiveContinent.objects.all()
    serializer_class = COVIDGlobalContinentSerializer
