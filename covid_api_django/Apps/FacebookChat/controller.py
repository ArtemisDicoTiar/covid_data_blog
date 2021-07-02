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
        return Response('SUCCESS')

    @staticmethod
    def get_message():
        return Response("You are stunning!")

    def trigger_post(self, request):
        output = request
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = self.get_message()
                        self.send_message(recipient_id, response_sent_text)
                    # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = self.get_message()
                        self.send_message(recipient_id, response_sent_nontext)
