import datetime

import coreapi
import coreschema
# from django_rest_params.decorators import params

from Apps.common.services import Params, BaseService
from rest_framework.schemas import ManualSchema


class CSSEService(BaseService):
    params = [
        Params(name='startDate', dtype=str, required=True,
               location='query', description="Query start date (format: %Y-%m-%d)"),
        Params(name='offset', dtype=int, required=True,
               location='query', description="The number of dates from startDate."),
    ]
    methods = ['get']

    def __init__(self, filterRegion):
        if filterRegion.lower() == 'country':
            self.params.append(
                Params(name='CountryCode', dtype=str, required=True,
                       location='query', description="Country's ISO code. (ISO3)"),
            )

        elif filterRegion.lower() == 'continent':
            self.params.append(
                Params(name='ContinentName', dtype=str, required=True,
                       location='query', description="ContinentName"),
            )
        self.params = self.params[::-1]

        super().__init__()

    @staticmethod
    def get_linearised_data(serialiser):
        return {
            key: [
                serialiser.data[row][key]
                for row in range(serialiser.data)
            ]
            for key in serialiser.child.fields
        }

    # @staticmethod
    # def param():
    #     return params()