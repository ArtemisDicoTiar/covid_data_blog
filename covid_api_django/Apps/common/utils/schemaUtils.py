from rest_framework.schemas import ManualSchema, coreapi, AutoSchema

from Apps.common.services import Params


def append_fields(schema: ManualSchema, param: Params):
    schema._fields.append(
        coreapi.Field(
            name=param.name,
            required=param.required,
            location=param.location,
            schema=param.get_schema(),
        ),
    )


# 뷰 함수별로 다른 스키마 적용

class CustomProfileSchema(AutoSchema):
    manual_fields = []  # common fields

    def get_manual_fields(self, path, method):
        custom_fields = []
        if method.lower() == "get":
            custom_fields = [
                coreapi.Field(
                    "username",
                    required=True,
                    location='form',
                    description='Username of the user '
                ),
                coreapi.Field(
                    "bio",
                    required=True,
                    location='form',
                    description='Bio of the user'
                ),
            ]
        if method.lower() == "post":
            custom_fields = [
                coreapi.Field(
                    "username",
                    required=True,
                    location='query',
                    description='Username of the user'
                ),
            ]
        return self._manual_fields + custom_fields
