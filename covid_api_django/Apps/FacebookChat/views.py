from datetime import timedelta, datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from route_decorator import Route

import secrets_app
from Apps.FacebookChat.controller import FaceBookChatBot_controller
from Apps.FacebookChat.services import FacebookChatBot_Webhook_Service
from Apps.common.utils.params import params


route = Route('/facebook')


@route('/chat', 'facebook_chatbot')
class GlobalRegionSearch_View(viewsets.ViewSet, ):
    service = FacebookChatBot_Webhook_Service()

    schema = service.schema

    controller = FaceBookChatBot_controller()

    @action(methods=service.methods, detail=False)
    def webhook(self, *args, **kwargs):
        if args[0].method == 'GET':
            if len(args[0].query_params) > 0:
                mode = args[0].query_params['hub.mode']
                challenge = args[0].query_params['hub.challenge']
                verify_token = args[0].query_params['hub.verify_token']

                return self.controller.verify_token(verify_token, challenge)

        if args[0].method == 'POST':
            return self.controller.trigger_post(args[0].data)

