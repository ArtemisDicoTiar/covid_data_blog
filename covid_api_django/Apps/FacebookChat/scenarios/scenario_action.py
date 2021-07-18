import json
from http import HTTPStatus

import requests

import secrets_app


def _get_country_page(content):
    return int(content['postback']['payload'].split('_')[-1])


def _write_message(payload, message):
    payload['message'] = message


def _get_user_info(user_id):
    req_point = 'https://graph.facebook.com/v11.0/{user_id}'.format(user_id=user_id)

    response = requests.get(
        req_point,
        params={
            'fields': 'id,name,locale,timezone',
            'access_token': secrets_app.FACEBOOK_CHAT_ACCESS_TOKEN
        }
    )

    return response


def _save_user_info(user_data):
    req_point = 'http://localhost:8000/api/facebook/users/info/'

    # user_data saved check
    response = requests.get(req_point, params=user_data)

    if response.status_code == HTTPStatus.BAD_REQUEST:  # should POST
        return requests.post(req_point, params=user_data)

    else:
        if json.loads(response.content) != user_data:  # should PUT
            return requests.put(req_point, params=user_data)

    return response


def _delete_user_info(user_data):
    req_point = 'http://localhost:8000/api/facebook/users/info/'

    # user_data saved check
    response = requests.get(req_point, params=user_data)

    if response.status_code == HTTPStatus.OK:
        return requests.delete(req_point, params=user_data)

    return response
