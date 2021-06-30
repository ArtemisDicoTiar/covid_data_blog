from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from Apps.common.services import Params, BaseService


class OWIDDataService(BaseService):
    def __init__(self):
        self.dropped_keys = []
        self.single_keys = ['code', 'continent',
                            'population',
                            'population_density',
                            'median_age',
                            'aged_65_older',
                            'aged_70_older',
                            'gdp_per_capita',
                            'extreme_poverty',
                            'cardiovasc_death_rate',
                            'diabetes_prevalence',
                            'female_smokers',
                            'male_smokers',
                            'hospital_beds_per_thousand',
                            'life_expectancy',
                            'human_development_index',
                            ]

        self.params = [
            Params(name='regionCode', dtype=str, required=True,
                   location='query', description="Region code (ISO3)"),
            Params(name='startDate', dtype=str, required=True,
                   location='query', description="Query start date (format: %Y-%m-%d)"),
            Params(name='offset', dtype=int, required=True,
                   location='query', description="The number of dates from startDate."),
        ]
        self.methods = ['get']

        super(OWIDDataService, self).__init__(params=self.params, methods=self.methods,
                                              dropped_keys=self.dropped_keys, single_keys=self.single_keys)

        self.schema = OWIDSchema(self.fields)


class OWIDMetaService(BaseService):
    def __init__(self):
        self.dropped_keys = []
        self.single_keys = []

        self.params = [
            Params(name='regionCode', dtype=str, required=True,
                   location='query', description="Region code (ISO3)"),
        ]
        self.methods = ['get']

        super(OWIDMetaService, self).__init__(params=self.params, methods=self.methods,
                                              dropped_keys=self.dropped_keys, single_keys=self.single_keys)

        self.schema = OWIDSchema(self.fields)

    def get_linearised_data(self, serialiser):
        if len(serialiser.data) == 0:
            return HttpResponseBadRequest("Requested Data not found")

        return Response(dict(
                map(lambda key: (
                    (key, serialiser.data[0][key])
                    if key not in self.dropped_keys and key not in self.single_keys
                    else (
                        (key, serialiser.data[0][key])
                        if key in self.single_keys
                        else None
                    )
                ), serialiser.child.fields)
        ))


class OWIDSchema(AutoSchema):
    manual_fields = []  # common fields

    def __init__(self, fields):
        super().__init__()
        self.manual_fields = fields

    def get_manual_fields(self, path, method):
        super().get_manual_fields(path, method)
        custom_fields = []
        # if path.lower() == "/api/covid/uk/prediction/":
        #     predDate_params = Params(name='predictedDate', dtype=str, required=True,
        #                              location='query', description="Target predicted date (format: %Y-%m-%d)")
        #     custom_fields = [
        #         coreapi.Field(
        #             name=predDate_params.name,
        #             required=predDate_params.required,
        #             location=predDate_params.location,
        #             schema=predDate_params.get_schema(),
        #         ),
        #     ]
        return self.manual_fields + custom_fields
