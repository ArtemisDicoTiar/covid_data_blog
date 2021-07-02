import json

import requests
from pymessenger import Bot
from rest_framework.response import Response

import secrets_app


class FaceBookChatBot_controller:
    # bot = Bot(access_token=secrets_app.FACEBOOK_CHAT_ACCESS_TOKEN)

    @staticmethod
    def verify_token(received_token, challenge):
        if received_token == secrets_app.FACEBOOK_CHAT_VERIFY_TOKEN:
            return Response(int(challenge))
        return Response('INVALID VERIFICATION TOKEN')

    @staticmethod
    def send_message(recipient_id, response):
        FB_API_URL = 'https://graph.facebook.com/v11.0/me/messages'

        payload = {
            'message': {
                'text': response
            },
            'recipient': {
                'id': recipient_id
            },
            'messaging_type': 'RESPONSE'
        }
        # json.dumps()

        auth = {
            'access_token': secrets_app.FACEBOOK_CHAT_ACCESS_TOKEN
        }

        response = requests.post(
            FB_API_URL,
            params=auth,
            json=payload
        )
        return Response(response)

    @staticmethod
    def get_message():
        return "You are stunning!"

    def trigger_post(self, request):
        output = request
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if 'message' in message.keys():
                    sender = message['sender']['id']
                    recipient = message['recipient']['id']

                    if 'text' in message['message'].keys():
                        text = message['message']['text']
                        response_sent_text = self.get_message()
                        return self.send_message(sender, response_sent_text + ':' + text)

                    elif 'attachments' in message.keys():
                        attached_item = message['attachments']['payload']
                        attached_type = message['attachments']['type']

                        response_sent_text = self.get_message()
                        return self.send_message(sender, response_sent_text + ':' + attached_type)

                else:
                    return Response("Error")
            else:
                return Response("NO MESSAGE")
        else:
            return Response("NO ENTRY")


