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
        return Response(self.bot.send_message(recipient_id, response))

    @staticmethod
    def get_message():
        return Response("You are stunning!")

    def trigger_post(self, request):
        output = request
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if 'message' in message.keys():
                    sender = message['sender']['id']
                    recipient = message['recipient']['id']
                    message = message['message']['text']
                    response_sent_text = self.get_message()
                    return self.send_message(recipient, response_sent_text)
