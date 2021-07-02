from datetime import timedelta, datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from route_decorator import Route

import secrets_app
from Apps.FacebookChat.services import FacebookChatBot_Webhook_Service
from Apps.common.utils.params import params

route = Route('/facebook')


@route('/chat', 'facebook_chatbot')
class GlobalRegionSearch_View(viewsets.ViewSet, ):
    service = FacebookChatBot_Webhook_Service()

    schema = service.schema

    @action(methods=service.methods, detail=False)
    # @params()
    def webhook(self, *args, **kwargs):
        print(args)
        print(kwargs)

        return Response("")

