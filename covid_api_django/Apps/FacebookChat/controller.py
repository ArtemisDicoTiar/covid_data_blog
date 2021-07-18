from http import HTTPStatus

import requests
from rest_framework.response import Response

import secrets_app
from Apps.FacebookChat.scenarios.Scenario import Scenario


class FaceBookChatBot_controller:

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
        return response

    def trigger_post(self, request):
        output = request
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                sender = message['sender']['id']
                recipient = message['recipient']['id']  # chatbot server

                return self.send_message(self.communicate(message, sender))

            else:
                return Response("NO MESSAGE", status=500)
        else:
            return Response("NO ENTRY", status=500)

    @staticmethod
    def communicate(content, user_id):
        scenario = Scenario(user_id=user_id)
        current_scenario = scenario.get_current_scenario(content)
        page_num = scenario.get_page_num(current_scenario, content)
        payload = scenario.write_response(current_scenario, page_num)

        return payload
