from __future__ import absolute_import, print_function
import requests
import json
from argparse import ArgumentParser


class PushoverException(Exception):
    pass


class PushoverResult(object):

    def __init__(self, code, text, data, params=None):
        self._code = code
        self._text = text
        self._params = params
        self._data = data

    def is_success(self):
        return self.code == 200 and self.status == 1

    @property
    def code(self):
        return self._code

    @property
    def status(self):
        return (self.data or {}).get('status', 0)

    @property
    def text(self):
        return self._text

    @property
    def params(self):
        return self._params

    @property
    def data(self):
        return self._data

    @property
    def json(self):
        return json.dumps(self.data)

    def __repr__(self):
        return '{0}(code={1}, text={2})'.format(self.__class__.__name__,
                                                self.code,
                                                self.text)


class Pushover(object):

    api_url = 'https://api.pushover.net'
    sounds = ('pushover', 'bike', 'bugle', 'cashregister', 'classical',
              'cosmic', 'falling', 'gamelan', 'incoming', 'intermission',
              'magic', 'mechanical', 'pianobar', 'siren', 'spacealarm',
              'tugboat', 'alien', 'climb', 'persistent', 'echo', 'updown',
              'none')

    def __init__(self, app_token, api_url=None):
        if api_url is not None:
            self.api_url = str(api_url)
        self.app_token = str(app_token)

    def send_message(self, key, message,
                     device=None, title=None, url=None, url_title=None,
                     sound=None, priority=0,
                     retry=None, expire=None, callback=None):
        data = {
            'token': self.app_token,
            'user': str(key),
            'message': str(message),
            'priority': int(priority),
        }
        if device is not None:
            data['device'] = str(device)
        if title is not None:
            data['title'] = str(title)
        if url is not None:
            data['url'] = str(url)
        if url_title is not None:
            data['url_title'] = str(url_title)
        if sound is not None:
            data['sound'] = str(sound)
        if priority == 2:
            data['retry'] = int(retry)
            data['expire'] = int(expire)
            if callback is not None:
                data['callback'] = str(callback)

        result = requests.post(self.api_url + '/1/messages.json', data=data)
        return PushoverResult(result.status_code, result.text, params=data)

    def get_receipt(self, receipt_id):

        result = requests.get('{0}/1/receipts/{1}.json'
                              .format(self.api_url, receipt_id),
                              params={'token': self.app_token})
        return PushoverResult(result.status_code, result.text, result.json(),
                              params={'receipt': receipt_id})

