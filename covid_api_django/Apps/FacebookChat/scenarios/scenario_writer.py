import json
from http import HTTPStatus

from pprint import pprint as pp

from Apps.FacebookChat.scenarios.scenario_action import _write_message, _get_user_info, _save_user_info, \
    _delete_user_info, _get_timezone
from Apps.FacebookChat.scenarios.utils.region import get_country_list
from Apps.common.utils.GeoInfoConvertor import convert_code_from_3_to_2


class ScenarioWriter:
    def __init__(self):
        self._user_id = None
        self._json_scenario = json.load(open('./scenarios.json'))

    def write_response(self, current_scenario, page_num=None, countryCode=None):
        def _construct_payload():
            return {
                'recipient': {'id': int(self._user_id)},
                'messaging_type': 'RESPONSE',
                'message': {},
            }

        payload = _construct_payload()

        # GET_STARTED
        if current_scenario == 1:
            _write_message(payload, self._json_scenario['get_started'])

        # CONTINENT_VIEW (SUBSCRIBE START)
        elif current_scenario == 21:
            _write_message(payload, self._json_scenario['continent_selection'])

        # COUNTRY VIEWS
        elif 221 <= current_scenario <= 225:
            country_quick_reply_obj = self._json_scenario['country_selection']
            if current_scenario == 221:
                country_quick_reply_obj['quick_replies'] = get_country_list(continent='africa',
                                                                            countries=self._json_scenario['countries'],
                                                                            page=page_num)
            elif current_scenario == 222:
                country_quick_reply_obj['quick_replies'] = get_country_list(continent='america',
                                                                            countries=self._json_scenario['countries'],
                                                                            page=page_num)
            elif current_scenario == 223:
                country_quick_reply_obj['quick_replies'] = get_country_list(continent='asia',
                                                                            countries=self._json_scenario['countries'],
                                                                            page=page_num)
            elif current_scenario == 224:
                country_quick_reply_obj['quick_replies'] = get_country_list(continent='europe',
                                                                            countries=self._json_scenario['countries'],
                                                                            page=page_num)
            elif current_scenario == 225:
                country_quick_reply_obj['quick_replies'] = get_country_list(continent='oceania',
                                                                            countries=self._json_scenario['countries'],
                                                                            page=page_num)
            _write_message(payload, country_quick_reply_obj)

        # COUNTRY selected
        elif current_scenario == 23:
            user_data_response = _get_user_info(user_id=self._user_id)

            # user data request failed.
            if user_data_response.status_code != HTTPStatus.OK:
                _write_message(payload, self._json_scenario['subscribe']['user_info_request_fail'])

            else:
                user_data = json.loads(user_data_response.content)
                timezone = _get_timezone(countryCode)
                conv_countryCode = convert_code_from_3_to_2(countryCode)

                user_data['locale'] = '_' + str(conv_countryCode)
                user_data['timezone'] = int(timezone)

                save_response = _save_user_info(user_data=user_data)

                if save_response.status_code != HTTPStatus.OK:
                    _write_message(payload, self._json_scenario['subscribe']['server_error'])

                else:
                    _write_message(payload, self._json_scenario['subscribe']['success'])

        # Unsubscribe result
        elif current_scenario == 3:
            user_data_response = _get_user_info(user_id=self._user_id)

            # user data request failed.
            if user_data_response.status_code != HTTPStatus.OK:
                _write_message(payload, self._json_scenario['unsubscribe']['user_info_request_fail'])

            else:
                user_data = json.loads(user_data_response.content)
                delete_response = _delete_user_info(user_data=user_data)

                if delete_response.status_code != HTTPStatus.OK:
                    _write_message(payload, self._json_scenario['unsubscribe']['server_error'])

                else:
                    _write_message(payload, self._json_scenario['unsubscribe']['success'])

        # Error
        # Others
        elif current_scenario == 40:
            _write_message(payload, self._json_scenario['error']['others'])

        # Message
        elif current_scenario == 41:
            _write_message(payload, self._json_scenario['error']['message'])

        # PostBack
        elif current_scenario == 42:
            _write_message(payload, self._json_scenario['error']['postback'])

        # Others
        else:
            pp(payload)
            raise IndexError("This Scenario cannot be triggered.")

        return payload
