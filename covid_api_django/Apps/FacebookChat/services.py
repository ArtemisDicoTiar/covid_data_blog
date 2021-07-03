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
            Params(name='hub.mode', dtype=str, required=False,
                   location='query', description="mode"),
            Params(name='hub.challenge', dtype=str, required=False,
                   location='query', description="challenge code"),
            Params(name='hub.verify_token', dtype=str, required=False,
                   location='query', description="verification code"),
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


class FacebookSubscription_Service(BaseService):
    def __init__(self):
        self.dropped_keys = []
        self.single_keys = [
            'recipient_id',
            'name',
            'locale',
            'timezone',
        ]

        self.params = [
            Params(name='id', dtype=str, required=True,
                   location='query', description="user id"),
            Params(name='name', dtype=str, required=False,
                   location='query', description="user name"),
            Params(name='locale', dtype=str, required=False,
                   location='query', description="locale code"),
            Params(name='timezone', dtype=int, required=False,
                   location='query', description="timezone"),
        ]
        self.methods = ['get', 'put', 'post', 'delete']

        super(FacebookSubscription_Service, self).__init__(params=self.params, methods=self.methods,
                                                           dropped_keys=self.dropped_keys,
                                                           single_keys=self.single_keys)
        self.schema = FacebookChatBot_Schema(self.fields)


class FacebookChatBot_Schema(AutoSchema):
    manual_fields = []  # common fields

    def __init__(self, fields):
        super().__init__()
        self.manual_fields = fields

    def get_manual_fields(self, path, method):
        super().get_manual_fields(path, method)
        custom_fields = []

        return self.manual_fields + custom_fields
