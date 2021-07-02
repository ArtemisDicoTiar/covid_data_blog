import coreapi
from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from Apps.common.services import Params, BaseService


class FacebookChatBot_Webhook_Service(BaseService):
    def __init__(self):
        self.dropped_keys = []
        self.single_keys = []

        self.params = [
            # Params(name='offset', dtype=int, required=True,
            #        location='query', description="The number of dates from startDate."),
            # Params(name='startDate', dtype=str, required=True,
            #        location='query', description="Query start date (format: %Y-%m-%d)"),
        ]
        self.methods = ['get', 'post']

        super(FacebookChatBot_Webhook_Service, self).__init__(params=self.params, methods=self.methods,
                                                              dropped_keys=self.dropped_keys,
                                                              single_keys=self.single_keys)
        self.schema = FacebookChatBot_Schema(self.fields)

    def get_linearised_data(self, query):
        if len(query) == 0:
            return HttpResponseBadRequest("Requested Data not found")

        return Response(query)


class FacebookChatBot_Schema(AutoSchema):
    manual_fields = []  # common fields

    def __init__(self, fields):
        super().__init__()
        self.manual_fields = fields

    def get_manual_fields(self, path, method):
        super().get_manual_fields(path, method)
        custom_fields = []

        return self.manual_fields + custom_fields
