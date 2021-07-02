import json

from pymessenger.bot import Bot
from rest_framework.response import Response

import secrets_app


class FaceBookChatBot_controller:
    bot = Bot(secrets_app.FACEBOOK_CHAT_ACCESS_TOKEN)

    @staticmethod
    def verify_token(received_token, challenge):
        if received_token == secrets_app.FACEBOOK_CHAT_VERIFY_TOKEN:
            return Response(int(challenge))
        return Response('INVALID VERIFICATION TOKEN')

    def send_message(self, recipient_id, response):
        self.bot.send_text_message(recipient_id, response)
        return 'SUCCESS'

