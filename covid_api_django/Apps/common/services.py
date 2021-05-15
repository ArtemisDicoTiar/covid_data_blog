import typing
from dataclasses import dataclass

import coreapi
import coreschema
from rest_framework.schemas import ManualSchema


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
    params: [[Params]] = list()
    fields = list()
    methods: [[str]] = list()

    def __init__(self):
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

        self.schema = ManualSchema(fields=self.fields)
