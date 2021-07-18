import json

from pprint import pprint as pp

from Apps.FacebookChat.scenarios.scenario_action import _write_message
from Apps.FacebookChat.scenarios.utils.region import get_country_list


class ScenarioWriter:
    def __init__(self):
        self._user_id = None
        self._json_scenario = json.load(open('./scenarios.json'))

    def write_response(self, current_scenario, page_num=None):
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

        # Subscription result
        elif 201 <= current_scenario <= 203:
            if current_scenario == 201:
                _write_message(payload, self._json_scenario['subscribe']['success'])

            elif current_scenario == 202:
                _write_message(payload, self._json_scenario['subscribe']['user_info_request_fail'])

            elif current_scenario == 203:
                _write_message(payload, self._json_scenario['subscribe']['server_error'])

        # Unsubscribe result
        elif 301 <= current_scenario <= 303:
            if current_scenario == 301:
                _write_message(payload, self._json_scenario['unsubscribe']['success'])

            elif current_scenario == 302:
                _write_message(payload, self._json_scenario['unsubscribe']['user_info_request_fail'])

            elif current_scenario == 303:
                _write_message(payload, self._json_scenario['unsubscribe']['server_error'])

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
