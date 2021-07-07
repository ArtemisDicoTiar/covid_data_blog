from datetime import timedelta, datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from route_decorator import Route

from Apps.OWID.serializers import *
from Apps.OWID.services import *
from Apps.common.utils.params import params

# Create your views here.

route = Route('/owid')


@route('/data', 'OWID_info')
class OWIDDataView(viewsets.ViewSet, ):
    service = OWIDDataService()

    schema = service.schema

    @action(methods=service.methods, detail=False)
    @params(regionCode=str,
            startDate=str,
            offset=int)
    def health(self, *args, **kwargs):
        code = kwargs['regionCode']
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        queryset = OWID_health.objects \
            .filter(iso_code=code,
                    date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                 (datetime.strptime(startDate, '%Y-%m-%d')
                                  + timedelta(days=offset - 1)).date())
                    )

        serializer_class = OWID_healthSerializer(queryset, many=True)

        return self.service.get_linearised_data(serializer_class)

    @action(methods=service.methods, detail=False)
    @params(regionCode=str,
            startDate=str,
            offset=int)
    def mortality(self, *args, **kwargs):
        code = kwargs['regionCode']
        # startDate = kwargs['startDate']
        # offset = kwargs['offset']

        queryset = OWID_mortality.objects \
            .filter(iso_code=code,
                    p_scores_all_ages__isnull=False,
                    ) \
            .latest('date')

        serializer_class = OWID_mortalitySerializer(queryset, many=False)

        return self.service.get_linearised_mortality_data(serializer_class)

    @action(methods=service.methods, detail=False)
    @params(regionCode=str,
            startDate=str,
            offset=int)
    def testing(self, *args, **kwargs):
        code = kwargs['regionCode']
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        queryset = OWID_testing_data.objects \
            .filter(ISO_code=code,
                    Date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                 (datetime.strptime(startDate, '%Y-%m-%d')
                                  + timedelta(days=offset - 1)).date()
                                 )
                    )
        serializer_class = OWID_testing_dataSerializer(queryset, many=True)

        return self.service.get_linearised_data(serializer_class)

    @action(methods=service.methods, detail=False)
    @params(regionCode=str,
            startDate=str,
            offset=int)
    def vaccination(self, *args, **kwargs):
        code = kwargs['regionCode']
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        queryset = OWID_vaccination_data.objects \
            .filter(iso_code__exact=code,
                    date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                 (datetime.strptime(startDate, '%Y-%m-%d')
                                  + timedelta(days=offset - 1)).date()
                                 )
                    )
        serializer_class = OWID_vaccination_dataSerializer(queryset, many=True)

        return self.service.get_linearised_data(serializer_class)


@route('/meta', 'testing')
class OWIDMetaView(viewsets.ViewSet, ):
    service = OWIDMetaService()

    schema = service.schema

    @action(methods=service.methods, detail=False)
    @params(regionCode=str)
    def testing(self, *args, **kwargs):
        code = kwargs['regionCode']

        queryset = OWID_testing_meta.objects \
            .filter(ISO_code__exact=code)
        serializer_class = OWID_testing_metaSerializer(queryset, many=True)

        return self.service.get_linearised_data(serializer_class)

    @action(methods=service.methods, detail=False)
    @params(regionCode=str)
    def vaccination(self, *args, **kwargs):
        code = kwargs['regionCode']

        queryset = OWID_vaccination_meta.objects \
            .filter(iso_code__exact=code)
        serializer_class = OWID_vaccination_metaSerializer(queryset, many=True)

        return self.service.get_linearised_data(serializer_class)
