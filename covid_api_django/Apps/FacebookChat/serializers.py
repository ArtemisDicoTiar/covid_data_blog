from rest_framework import serializers

from Apps.FacebookChat.models import FacebookSubscription_model


class FacebookSubscription_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookSubscription_model
        fields = [
            'recipient_id',
            'name',
            'locale',
            'timezone',
        ]
