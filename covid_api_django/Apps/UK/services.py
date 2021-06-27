import coreapi
from rest_framework.schemas import AutoSchema

from Apps.common.services import Params, BaseService


class UKService(BaseService):

    def __init__(self):
        self.dropped_keys = []
        self.single_keys = ['code', 'name', 'areaType']

        self.params = [
            Params(name='regionCode', dtype=str, required=True,
                   location='query', description="UK region code"),
            Params(name='startDate', dtype=str, required=True,
                   location='query', description="Query start date (format: %Y-%m-%d)"),
            Params(name='offset', dtype=int, required=True,
                   location='query', description="The number of dates from startDate."),
        ]
        self.methods = ['get']

        super(UKService, self).__init__(params=self.params, methods=self.methods,
                                        dropped_keys=self.dropped_keys, single_keys=self.single_keys)

        self.schema = UKSchema(self.fields)


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
