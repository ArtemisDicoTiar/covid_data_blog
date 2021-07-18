import coreapi
from rest_framework.schemas import AutoSchema

from Apps.common.services import Params, BaseService


class CSSEService(BaseService):
    def __init__(self, filterRegion):
        self.dropped_keys = []
        self.single_keys = ['CountryCode', 'ContinentName', 'predicted']

        self.params = [
            Params(name='offset', dtype=int, required=True,
                   location='query', description="The number of dates from startDate."),
            Params(name='startDate', dtype=str, required=True,
                   location='query', description="Query start date (format: %Y-%m-%d)"),
        ]
        self.methods = ['get']

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

        super(CSSEService, self).__init__(params=self.params, methods=self.methods,
                                          dropped_keys=self.dropped_keys, single_keys=self.single_keys)
        self.schema = CSSESchema(self.fields)


class CSSESchema(AutoSchema):
    manual_fields = []  # common fields

    def __init__(self, fields):
        super().__init__()
        self.manual_fields = fields

    def get_manual_fields(self, path, method):
        super().get_manual_fields(path, method)
        custom_fields = []
        if path.lower() == "/api/covid/global/prediction/" or path.lower() == "/api/covid/global/lstm_prediction/":
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
