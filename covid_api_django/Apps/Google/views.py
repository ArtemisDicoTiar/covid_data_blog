from datetime import timedelta, datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from route_decorator import Route

from Apps.Google.models import Google_Mobility
from Apps.Google.serializers import Google_MobilitySerializer
from Apps.Google.services import GoogleMobility_Service
from Apps.common.utils.params import params

route = Route('/google')


@route('/mobility', 'google_mobility')
class GoogleMobility_View(viewsets.ViewSet, ):
    service = GoogleMobility_Service()

    schema = service.schema

    @action(methods=service.methods, detail=False)
    @params(regionCode=str,
            startDate=str,
            offset=int)
    def info(self, *args, **kwargs):
        CountryCode = kwargs['regionCode']
        startDate = kwargs['startDate']
        offset = kwargs['offset']

        queryset = Google_Mobility.objects \
            .filter(CountryCode=CountryCode,
                    date__range=(datetime.strptime(startDate, '%Y-%m-%d').date(),
                                 (datetime.strptime(startDate, '%Y-%m-%d')
                                  + timedelta(days=offset - 1)).date()
                                 ),
                    )

        serializer_class = Google_MobilitySerializer(queryset, many=True)

        return self.service.get_linearised_data(serializer_class)

