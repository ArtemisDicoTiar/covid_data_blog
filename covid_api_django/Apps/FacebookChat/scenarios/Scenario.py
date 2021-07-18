from Apps.FacebookChat.scenarios.CurrentScenario import ScenarioStatus
from Apps.FacebookChat.scenarios.scenario_reader import ScenarioReader
from Apps.FacebookChat.scenarios.scenario_writer import ScenarioWriter


class Scenario(ScenarioStatus, ScenarioReader, ScenarioWriter):
    def __init__(self, user_id):
        super().__init__()
        self._user_id = user_id


if __name__ == '__main__':
    scenario = Scenario(1234)
    scenario.write_response(21, 1)


