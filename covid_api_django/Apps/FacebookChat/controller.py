import json
from datetime import date
from http import HTTPStatus
from pprint import pprint as pp

import requests
from pymessenger import Bot
from rest_framework.response import Response

import secrets_app


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
        return Response(data=response.content, status=response.status_code)

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

        def _get_user_info(user_id):
            req_point = 'https://graph.facebook.com/v11.0/{user_id}'.format(user_id=user_id)

            params = {
                'fields': 'id,name,locale,timezone',
                'access_token': secrets_app.FACEBOOK_CHAT_ACCESS_TOKEN
            }

            response = requests.get(
                req_point,
                params=params,
            )

            return response

        def _save_user_info(user_data):
            req_point = 'http://localhost:8000/api/facebook/users/info/'

            # user_data saved check
            response = requests.get(
                req_point,
                params=user_data,
            )

            if response.status_code == HTTPStatus.BAD_REQUEST:
                # should PUT
                return requests.post(
                    req_point,
                    params=user_data
                )

            else:
                if json.loads(response.content) != user_data:
                    # should post
                    return requests.put(
                        req_point,
                        params=user_data
                    )

            return response

        def _delete_user_info(user_data):
            req_point = 'http://localhost:8000/api/facebook/users/info/'

            # user_data saved check
            response = requests.get(
                req_point,
                params=user_data,
            )

            if response.status_code == HTTPStatus.OK:
                # should PUT
                return requests.delete(
                    req_point,
                    params=user_data
                )

            return response

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

            # subscribe
            elif content['postback']['payload'] == 'subscribe':
                user_data_response = _get_user_info(user_id=user_id)

                # user data request failed.
                if user_data_response.status_code != HTTPStatus.OK:
                    payload['message'] = {
                        'text': 'Your user information request failed. Subscription is unavailable.'
                    }

                else:
                    user_data = json.loads(user_data_response.content)
                    save_response = _save_user_info(user_data=user_data)

                    if save_response.status_code != HTTPStatus.OK:
                        payload['message'] = {
                            'text': 'Server Database Error. Please contact server manager.'
                        }

                    else:
                        payload['message'] = {
                            'text': 'Successfully subscribed. Every 10AM you will receive latest information.'
                        }

            # unsubscribe
            elif content['postback']['payload'] == 'unsubscribe':
                user_data_response = _get_user_info(user_id=user_id)

                # user data request failed.
                if user_data_response.status_code != HTTPStatus.OK:
                    payload['message'] = {
                        'text': 'Your user information request failed. Subscription is unavailable.'
                    }
                else:
                    user_data = json.loads(user_data_response.content)
                    delete_response = _delete_user_info(user_data=user_data)

                    if delete_response.status_code != HTTPStatus.OK:
                        payload['message'] = {
                            'text': 'Server Database Error. Please contact server manager.'
                        }

                    else:
                        payload['message'] = {
                            'text': 'Successfully subscription cancelled.'
                        }

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
