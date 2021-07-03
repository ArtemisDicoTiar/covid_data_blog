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
                sender = message['sender']['id']
                recipient = message['recipient']['id']

                return self.send_message(self.get_response(message, sender))

            else:
                return Response("NO MESSAGE", status=500)
        else:
            return Response("NO ENTRY", status=500)

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
                    },{
                        "content_type": "text",
                        "title": "America",
                        "payload": "continent_America__",
                    },{
                        "content_type": "text",
                        "title": "TEST",
                        "payload": "continent_TEST__",
                    },
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
        pp(content)
        # postback button clicked
        if _is_postback(content):
            # greeting message
            if content['postback']['payload'] == 'get_started':
                payload['message'] = {
                    'text': 'Welcome to COVID notification chatbot.'
                }

            # subscribe / today dialog start
            elif content['postback']['payload'] == 'subscribe':
                payload['message'] = _request_query_region()

            elif content['postback']['payload'] == 'todayInfo':
                payload['message'] = _get_region_search_result()

            # sub_regions = json.loads(
            #     requests.get('http://localhost:8000/api/region/global/search/',
            #                  params={'regionName': 'province_name'}).content
            # )

            else:
                print('UNHANDLED POSTBACK')

        # message delivered
        elif _is_message(content):
            payload['message'] = {
                'text': 'Message Response is unavailable. Please use buttons next to text bar.'
            }

        else:
            payload['message'] = {
                'text': 'Error. (Enquiry to Server manager)'
            }
            print('UNHANDLED CONTENT')
            pp(content)

        return payload
