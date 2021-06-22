from datetime import datetime, timedelta


def prediction_parameter_validate(predictedDate: str, date: str, offset: int):
    if offset > 7:
        raise ValueError("Offset should be smaller than 7 days")

    if datetime.strptime(predictedDate, '%Y-%m-%d').date() > datetime.strptime(date, '%Y-%m-%d').date():
        raise ValueError("Predicted date should be earlier than date.")

    if (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=offset - 1)).date() \
            - datetime.strptime(predictedDate, '%Y-%m-%d').date() \
            > timedelta(days=7):
        raise ValueError("Only 7 days can be viewed from predicted date")
