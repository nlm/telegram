from __future__ import absolute_import, print_function
import requests
import json
from argparse import ArgumentParser


class TelegramException(Exception):
    pass


class Telegram(object):

    api_url = 'https://api.telegram.org'

    def __init__(self, bot_token, api_url=None):
        if api_url is not None:
            self.api_url = str(api_url)
        self.bot_token = str(bot_token)

    def send_message(self, chat_id, text, disable_notification=False):
        data = {
            'chat_id': chat_id,
            'text': text,
            'disable_notification': disable_notification
        }

        result = requests.post('{0}/bot{1}/sendMessage'
                               .format(self.api_url, self.bot_token),
                               data=data)

        return result.json().get('ok', False)
