from datetime import datetime, timedelta

from django.http import HttpResponseBadRequest


def prediction_parameter_validate(predictedDate: str, date: str, offset: int):
    if offset > 7:
        return HttpResponseBadRequest("Offset should be smaller than 7 days")

    if datetime.strptime(predictedDate, '%Y-%m-%d').date() > datetime.strptime(date, '%Y-%m-%d').date():
        return HttpResponseBadRequest("Predicted date should be earlier than date.")

    if (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=offset - 1)).date() \
            - datetime.strptime(predictedDate, '%Y-%m-%d').date() \
            > timedelta(days=7):
        return HttpResponseBadRequest("Only 7 days can be viewed from predicted date")
