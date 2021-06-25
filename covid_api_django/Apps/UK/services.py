import datetime

import coreapi
import coreschema

from Apps.common.services import Params, BaseService
from rest_framework.schemas import ManualSchema, AutoSchema


class UKService(BaseService):

    def __init__(self):
        self.params = [
            Params(name='regionCode', dtype=str, required=True,
                   location='query', description="UK region code"),
            Params(name='startDate', dtype=str, required=True,
                   location='query', description="Query start date (format: %Y-%m-%d)"),
            Params(name='offset', dtype=int, required=True,
                   location='query', description="The number of dates from startDate."),
        ]
        self.methods = ['get']

        super(UKService, self).__init__(params=self.params, methods=self.methods)

        self.schema = UKSchema(self.fields)

    @staticmethod
    def get_linearised_data(serialiser):
        dropped_keys = []
        single_keys = ['code', 'name', 'areaType']
        return dict(
            map(lambda key: (
                (key, map(lambda row_data: row_data[key], serialiser.data))
                if key not in dropped_keys and key not in single_keys
                else (
                    (key, serialiser.data[0][key])
                    if key in single_keys
                    else None
                )
            ),
                serialiser.child.fields)
        )


class UKSchema(AutoSchema):
    manual_fields = []  # common fields

    def __init__(self, fields):
        super().__init__()
        self.manual_fields = fields

    def get_manual_fields(self, path, method):
        super().get_manual_fields(path, method)
        custom_fields = []
        if path.lower() == "/api/covid/uk/prediction/":
            predDate_params = Params(name='predictedDate', dtype=str, required=True,
                                     location='query', description="Target predicted date (format: %Y-%m-%d)")
            custom_fields = [
                coreapi.Field(
                    name=predDate_params.name,
                    required=predDate_params.required,
                    location=predDate_params.location,
                    schema=predDate_params.get_schema(),
                ),
            ]
        return self.manual_fields + custom_fields
