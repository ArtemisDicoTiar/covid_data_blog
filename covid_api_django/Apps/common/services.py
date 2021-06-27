from dataclasses import dataclass

import coreapi
import coreschema
from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema


@dataclass
class Params:
    name: str
    required: bool
    location: str
    description: str
    dtype: object

    def get_schema(self):
        if self.dtype == str:
            return coreschema.String(description=self.description)

        elif self.dtype == bool:
            return coreschema.Boolean(description=self.description)

        elif self.dtype == int:
            return coreschema.Integer(description=self.description)
        elif self.dtype == float:
            return coreschema.Number(description=self.description)

        elif self.dtype == list:
            return coreschema.Array(description=self.description)

        else:
            raise TypeError("Parameter must have type.")


class BaseService:
    def __init__(self,
                 params: [[Params]],
                 methods: [[str]],
                 dropped_keys: [[str]],
                 single_keys: [[str]]):
        self.params: params
        self.methods: methods
        self.fields = list()

        self.dropped_keys = dropped_keys
        self.single_keys = single_keys

        for param in self.params:
            self.fields.append(
                coreapi.Field(
                    name=param.name,
                    required=param.required,
                    location=param.location,
                    schema=param.get_schema(),
                ),
            )

        for idx, method in enumerate(self.methods):
            self.methods[idx] = method.lower()

        self.schema = AutoSchema(manual_fields=self.fields)

    def get_linearised_data(self, serialiser):
        if len(serialiser.data) == 0:
            return HttpResponseBadRequest("Requested Data not found")

        return Response(dict(
                map(lambda key: (
                    (key, map(lambda row_data: row_data[key], serialiser.data))
                    if key not in self.dropped_keys and key not in self.single_keys
                    else (
                        (key, serialiser.data[0][key])
                        if key in self.single_keys
                        else None
                    )
                ), serialiser.child.fields)
        ))
