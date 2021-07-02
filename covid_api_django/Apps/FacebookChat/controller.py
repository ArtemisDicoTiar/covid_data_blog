import json

import requests
from rest_framework.response import Response

import secrets_app

from pprint import pprint as pp


class FaceBookChatBot_controller:

    @staticmethod
    def verify_token(received_token, challenge):
        if received_token == secrets_app.FACEBOOK_CHAT_VERIFY_TOKEN:
            return Response(int(challenge))
        return Response('INVALID VERIFICATION TOKEN')

    @staticmethod
    def send_message(recipient_id, response):
        FB_API_URL = 'https://graph.facebook.com/v11.0/me/'
        payload = {
            'message': {
                'text': response
            },
            'recipient': {
                'id': recipient_id
            },
            'notification_type': 'regular'
        }
            # json.dumps()

        auth = {
            'access_token': secrets_app.FACEBOOK_CHAT_ACCESS_TOKEN
        }

        response = requests.post(
            FB_API_URL,
            params=auth,
            data=payload
        )

        return Response(response)

    @staticmethod
    def get_message():
        return Response("You are stunning!")

    def trigger_post(self, request):
        output = request
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if 'message' in message.keys():
                    pp(message)
                    sender = message['sender']['id']
                    recipient = message['recipient']['id']
                    text = message['message']['text']
                    response_sent_text = self.get_message()
                    return self.send_message(recipient, response_sent_text)
                else:
                    return Response("Error")
            else:
                return Response("NO MESSAGE")
        else:
            return Response("NO ENTRY")
