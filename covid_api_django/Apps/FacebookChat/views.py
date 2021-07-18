from datetime import timedelta, datetime
from pprint import pprint as pp

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from route_decorator import Route

import secrets_app
from Apps.FacebookChat.controller import FaceBookChatBot_controller
from Apps.FacebookChat.models import FacebookSubscription_model
from Apps.FacebookChat.serializers import FacebookSubscription_Serializer
from Apps.FacebookChat.services import FacebookChatBot_Webhook_Service, FacebookSubscription_Service, \
    FacebookSubscriptionUsers_Service
from Apps.common.utils.params import params

route = Route('/facebook')


@route('/chat', 'facebook_chatbot')
class FacebookChatbot_View(viewsets.ViewSet, ):
    service = FacebookChatBot_Webhook_Service()

    schema = service.schema

    controller = FaceBookChatBot_controller()

    @action(methods=service.methods, detail=False)
    def webhook(self, *args, **kwargs):
        pp(args[0].data)
        if args[0].method == 'GET':
            if len(args[0].query_params) > 0:
                mode = args[0].query_params['hub.mode']
                challenge = args[0].query_params['hub.challenge']
                verify_token = args[0].query_params['hub.verify_token']

                return self.controller.verify_token(verify_token, challenge)

        if args[0].method == 'POST':
            return self.controller.trigger_post(args[0].data)


@route('/users', 'facebook_userinfo')
class FacebookSubscription_View(viewsets.ViewSet, ):
    service = FacebookSubscription_Service()

    schema = service.schema

    @action(methods=service.methods, detail=False)
    @params(id=str,
            name=str,
            locale=str,
            timezone=int)
    def info(self, *args, **kwargs):
        if args[0].method == 'GET':
            if len(args[0].query_params) > 0:
                recipient_id = kwargs['id']

                queryset = FacebookSubscription_model.objects \
                    .filter(recipient_id=recipient_id)

                serializer_class = FacebookSubscription_Serializer(queryset, many=True)

                return self.service.get_linearised_data(serializer_class)

        if args[0].method == 'PUT':
            instance = get_object_or_404(FacebookSubscription_model.objects.all(), pk=kwargs['id'])

            serializer_class = FacebookSubscription_Serializer(instance=instance,
                                                               data={
                                                                   'recipient_id': kwargs['id'],
                                                                   'name': kwargs['name'],
                                                                   'locale': kwargs['locale'],
                                                                   'timezone': kwargs['timezone'],
                                                               })

            if abs(kwargs['timezone']) > 12:
                return Response('timezone range error', status=500)

            if serializer_class.is_valid():
                serializer_class.save()

                return Response(serializer_class.validated_data)

            return Response('Error', status=500)

        if args[0].method == 'POST':
            serializer_class = FacebookSubscription_Serializer(instance=FacebookSubscription_model,
                                                               data={
                                                                   'recipient_id': kwargs['id'],
                                                                   'name': kwargs['name'],
                                                                   'locale': kwargs['locale'],
                                                                   'timezone': kwargs['timezone'],
                                                               })

            if abs(kwargs['timezone']) > 12:
                return Response('timezone range error', status=500)

            if serializer_class.is_valid():
                serializer_class.create(serializer_class.validated_data)
                return Response(serializer_class.validated_data)

            return Response('Error', status=500)

        if args[0].method == 'DELETE':
            try:
                FacebookSubscription_model.objects.get(recipient_id=kwargs['id']).delete()
                return Response(kwargs)

            except:
                return Response('Error', status=500)


@route('/timezone', 'facebook_userinfo_by_times')
class FacebookSubscriptionUsers_View(viewsets.ViewSet, ):
    service = FacebookSubscriptionUsers_Service()

    schema = service.schema

    @action(methods=service.methods, detail=False)
    @params(timezone=int)
    def users(self, *args, **kwargs):
        timezone = kwargs['timezone']
        queryset = FacebookSubscription_model.objects \
            .filter(timezone=timezone)

        serializer_class = FacebookSubscription_Serializer(queryset, many=True)

        return self.service.get_linearised_data(serializer_class)
