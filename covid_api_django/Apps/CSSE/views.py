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
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.schemas import AutoSchema, ManualSchema
from rest_framework.views import APIView
from route_decorator import Route

from Apps.CSSE.serializers import *
from Apps.CSSE.models import *
from route_decorator import Route

from Apps.CSSE.services import *

route = Route('/covid')


@route('/global', 'CSSE_CaseView')
class CSSE_CasesView(viewsets.ViewSet):
    service = CSSE_CaseService()

    schema = service.schema

    @service.actions()
    @service.parameters()
    def cases(self, request, *args, **kwargs):
        serializer_class = None
        if kwargs['regionType'] == 'country':
            quer = self.service.get_queryset(*args, **kwargs)
            serializer_class = CSSE_CasesCountrySerializer(
                self.service.get_queryset(*args, **kwargs), many=True
            )
        elif kwargs['regionType'] == 'continent':
            serializer_class = CSSE_CasesContinentSerializer(
                self.service.get_queryset(*args, **kwargs), many=True
            )

        return Response(self.service.get_linearised_data(serializer_class, *args, **kwargs))


@route('/global', 'CSSE_CasePredictionView')
class CSSE_CasesPredictionView(viewsets.ViewSet):
    service = CSSE_CasePredictionService()

    schema = service.schema

    @service.actions()
    @service.parameters()
    def predictedCases(self, request, *args, **kwargs):
        serializer_class = None
        if kwargs['regionType'] == 'country':
            serializer_class = CSSE_Cases_predictionCountrySerializer(
                self.service.get_queryset(*args, **kwargs), many=True
            )
        elif kwargs['regionType'] == 'continent':
            serializer_class = CSSE_Cases_predictionContinentSerializer(
                self.service.get_queryset(*args, **kwargs), many=True
            )

        return Response(self.service.get_linearised_data(serializer_class, *args, **kwargs))


@route('/global', 'CSSE_CasePredictionAccuracyView')
class CSSE_CasesPredictionView(viewsets.ViewSet):
    service = CSSE_CasePredictionAccuracyService()

    schema = service.schema

    @service.actions()
    @service.parameters()
    def predictedAccuracy(self, request, *args, **kwargs):
        serializer_class = None
        if kwargs['regionType'] == 'country':
            serializer_class = CSSE_Cases_prediction_accuracyCountrySerializer(
                self.service.get_queryset(*args, **kwargs), many=True
            )

        elif kwargs['regionType'] == 'continent':
            serializer_class = CSSE_Cases_prediction_accuracyContinentSerializer(
                self.service.get_queryset(*args, **kwargs), many=True
            )

        return Response(self.service.get_linearised_data(serializer_class, *args, **kwargs))
