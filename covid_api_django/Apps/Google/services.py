from rest_framework.schemas import AutoSchema

from Apps.common.services import Params, BaseService


class GoogleMobility_Service(BaseService):
    def __init__(self):
        self.dropped_keys = []
        self.single_keys = ['CountryName', 'CountryCode']

        self.params = [
            Params(name='regionCode', dtype=str, required=True,
                   location='query', description="Country code (ISO3)"),
            Params(name='startDate', dtype=str, required=True,
                   location='query', description="Query start date (format: %Y-%m-%d)"),
            Params(name='offset', dtype=int, required=True,
                   location='query', description="The number of dates from startDate."),

            # Params(name='retail_and_recreation', dtype=bool, required=True,
            #        location='header', description="requesting retail and recreation data"),
            # Params(name='grocery_and_pharmacy', dtype=bool, required=True,
            #        location='header', description="requesting grocery and pharmacy data"),
            # Params(name='parks', dtype=bool, required=True,
            #        location='header', description="requesting parks data"),
            # Params(name='transit_stations', dtype=bool, required=True,
            #        location='header', description="requesting transit stations data"),
            # Params(name='workplaces', dtype=bool, required=True,
            #        location='header', description="requesting workplaces data"),
            # Params(name='residential', dtype=bool, required=True,
            #        location='header', description="requesting residential data"),
        ]
        self.methods = ['get']

        super(GoogleMobility_Service, self).__init__(params=self.params, methods=self.methods,
                                                     dropped_keys=self.dropped_keys, single_keys=self.single_keys)
        self.schema = GoogleMobility_Schema(self.fields)


class GoogleMobility_Schema(AutoSchema):
    manual_fields = []  # common fields

    def __init__(self, fields):
        super().__init__()
        self.manual_fields = fields

    def get_manual_fields(self, path, method):
        super().get_manual_fields(path, method)
        custom_fields = []

        return self.manual_fields + custom_fields
