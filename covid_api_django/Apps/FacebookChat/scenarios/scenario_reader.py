from Apps.FacebookChat.scenarios.CurrentScenario import ScenarioStatus


class ScenarioReader:
    @staticmethod
    def get_page_num(scenario_num, content):
        if 221 <= scenario_num <= 225:
            return content['postback']['payload'].split('_')[-1]

        return None

    @staticmethod
    def get_current_scenario(content):
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

        if _is_postback(content):
            if content['postback']['payload'] == 'get_started':
                return ScenarioStatus.GET_STARTED

            elif content['postback']['payload'] == 'subscribe':
                return ScenarioStatus.Subscribe.ContinentView

            elif 'sub' in content['postback']['payload']:
                # country is selected
                if len(content['postback']['payload'].split('_')) == 4:
                    return ScenarioStatus.Subscribe.CountrySelected

                elif 'sub_asia' in content['postback']['payload']:
                    return ScenarioStatus.Subscribe.CountryView.Asia
                elif 'sub_america' in content['postback']['payload']:
                    return ScenarioStatus.Subscribe.CountryView.America
                elif 'sub_africa' in content['postback']['payload']:
                    return ScenarioStatus.Subscribe.CountryView.Africa
                elif 'sub_europe' in content['postback']['payload']:
                    return ScenarioStatus.Subscribe.CountryView.Europe
                elif 'sub_oceania' in content['postback']['payload']:
                    return ScenarioStatus.Subscribe.CountryView.Oceania

            elif content['postback']['payload'] == 'unsubscribe':
                return ScenarioStatus.Unsubscribe.Requested

            else:
                return ScenarioStatus.Error.PostBack

        elif _is_message(content):
            return ScenarioStatus.Error.Message

        else:
            return ScenarioStatus.Error.Others


