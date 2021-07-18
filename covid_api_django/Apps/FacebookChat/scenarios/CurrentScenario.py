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

        Success = 201
        Fail = 202
        ServerError = 203

    class Unsubscribe:
        Success = 301
        Fail = 302
        ServerError = 303

    class Error:
        Others = 40
        Message = 41
        PostBack = 42


if __name__ == '__main__':
    ...
