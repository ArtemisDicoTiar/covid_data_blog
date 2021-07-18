class ScenarioStatus:
    GET_STARTED = 1

    class Subscribe:
        ContinentView = 21

        class CountryView:
            Africa = 221
            America = 222
            Asia = 223
            Europe = 224
            Oceania = 225

        CountrySelected = 23

    class Unsubscribe:
        Requested = 3

    class Error:
        Others = 40
        Message = 41
        PostBack = 42


if __name__ == '__main__':
    ...
