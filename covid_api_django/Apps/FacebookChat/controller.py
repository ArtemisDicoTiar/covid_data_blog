import json
from pprint import pprint as pp

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
    def send_message(payload):
        FB_API_URL = 'https://graph.facebook.com/v11.0/me/messages'

        auth = {
            'access_token': secrets_app.FACEBOOK_CHAT_ACCESS_TOKEN
        }

        response = requests.post(
            FB_API_URL,
            params=auth,
            json=payload
        )
        return Response(response)

    def trigger_post(self, request):
        output = request
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if 'message' in message.keys():
                    sender = message['sender']['id']
                    recipient = message['recipient']['id']

                    return self.send_message(self.get_response(message, sender))
                    # if 'text' in message['message'].keys():
                    #     text = message['message']['text']
                    #     response_sent_text = self.get_message()
                    #     return self.send_message(sender, response_sent_text + ':' + text)
                    #
                    # elif 'attachments' in message.keys():
                    #     attached_item = message['attachments']['payload']
                    #     attached_type = message['attachments']['type']
                    #
                    #     response_sent_text = self.get_message()
                    #     return self.send_message(sender, response_sent_text + ':' + attached_type)

                else:
                    return Response("Error")
            else:
                return Response("NO MESSAGE")
        else:
            return Response("NO ENTRY")

    @staticmethod
    def get_response(content, user_id):
        def _construct_payload():
            return {
                'recipient': {'id': int(user_id)},
                'messaging_type': 'RESPONSE',
                'message': {},
            }

        def _is_postback(msg):
            if 'postback' in msg.keys():
                if 'payload' in msg['postback'].keys():
                    return True
            return False

        def _is_message(msg):
            if 'message' in msg.keys():
                if 'text' in msg['message'].keys():
                    return True
            return False

        def _request_query_region():
            return {
                "text": "Search your region:"
            }

        def _get_region_search_result():
            return {
                "text": "Pick where you live (continent):",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Africa",
                        "payload": "continent_Africa__",
                    }
                ]
            }

        def _get_user_info():
            ...

        def _get_today_info():
            ...

        def _get_subscription_response():
            ...

        # ============= MAIN LOGIC START ============= #
        payload = _construct_payload()

        # postback button clicked
        if _is_postback(content):
            print('postback')
            # greeting message
            if content['postback']['payload'] == 'get_started':
                payload['message'] = {
                    'text': 'Welcome to COVID notification chatbot.'
                }

            # subscribe / today dialog start
            elif content['postback']['payload'] == 'subscribe' \
                    or content['postback']['payload'] == 'todayInfo':
                ...


            else:
                print('UNHANDLED POSTBACK')
                pp(content)

        # message delivered
        elif _is_message(content):
            print('message')
            payload['message'] = {
                'text': 'Message Response is unavailable. Please use buttons below.'
            }

        else:
            print('UNHANDLED CONTENT')
            pp(content)
        print("THIS IS PAYLOAD")
        pp(payload)
        return payload
