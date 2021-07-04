import json
from datetime import datetime, timedelta
from http import HTTPStatus

import requests

import secrets_app
from Apps.common.utils.GeoInfoConvertor import get_country_iso_information


def send_daily_notification():
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

    today = datetime.now().date() - timedelta(days=3)
    current_hour = datetime.now().time().hour
    print('Daily Notification:', today, current_hour)

    res = requests.get(
        url='http://localhost:8000/api/facebook/timezone/users/',
        params={'timezone': current_hour - 10}
    )

    if res.status_code == HTTPStatus.OK:
        current_queue = json.loads(res.content)
        print('Daily Notification Targets:', current_queue)
        while current_queue:
            print('Remaining Queue:', current_queue)
            user_id, user_name, locale, timezone = current_queue.pop(0)

            country_obj = get_country_iso_information(locale.split('_')[-1])

            region_name = country_obj.name
            locale_iso3 = country_obj.alpha_3

            data_res = requests.get(
                url='http://localhost:8000/api/covid/global/cases/',
                params={
                    'CountryCode': locale_iso3,
                    'startDate': today,
                    'offset': 5,
                }
            )

            payload = {
                'recipient': {'id': int(user_id)},
                'messaging_type': 'RESPONSE',
                'message': {},
            }

            if data_res.status_code == HTTPStatus.OK:
                data = json.loads(data_res.content)
                new_confirmed_cases = int(data['confirmed'][-1]) - int(data['confirmed'][-2])
                latest_date = data['date'][-1]

                successMsg = payload.copy()
                successMsg['message'] = {
                    'text': 'COVID Confirmed Cases in {country} on {latest} is "{cases}"'
                        .format(country=region_name, latest=latest_date, cases=new_confirmed_cases)
                }
                send_message(successMsg)

            else:
                errorMsg = payload.copy()
                errorMsg['message'] = {
                    'text': 'COVID Data request failed. Please view detailed information on following website.'
                }
                send_message(errorMsg)

            website = payload.copy()

            website['message'] = {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Website for detailed information.",
                                "subtitle": "Detailed COVID related information can be found on this website",
                                "default_action": {
                                    "type": "web_url",
                                    "url": "http://covidgraph.johnjongyoonkim.com",
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "http://covidgraph.johnjongyoonkim.com",
                                        "title": "Visit Website"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
            send_message(website)


send_daily_notification()
