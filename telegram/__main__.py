from __future__ import absolute_import, print_function
import os
import sys
import requests
from argparse import ArgumentParser
from .__init__ import Telegram

def send_message(args):
    telegram = Telegram(args.telegram_bot_token)
    return telegram.send_message(args.chat_id, args.text)

def main():
    parser = ArgumentParser()

    parser.add_argument('-T', '--telegram-bot-token',
                        metavar='TELEGRAM_BOT_TOKEN',
                        help=("your bot's API token. "
                              "Can be defined in environment var "
                              "TELEGRAM_BOT_TOKEN"),
                        default=os.environ.get('TELEGRAM_BOT_TOKEN'))

    parser.add_argument('-f', '--format',
                        choices=('text', 'json'),
                        default='text',
                        help="program output format")

    subparsers = parser.add_subparsers()
    subparsers.required=True

    sm_p = subparsers.add_parser('send_message')
    sm_p.set_defaults(func=send_message)

    sm_p.add_argument('-i', '--chat-id', required=True, help=("the chat id"))
    sm_p.add_argument('-N', '--disable-notification', help="disable notification")
    sm_p.add_argument('-t', '--text', help="your text")

    args = parser.parse_args()

    requests.packages.urllib3.disable_warnings()

    if args.telegram_bot_token is None:
        parser.error('TELEGRAM_BOT_TOKEN is required')

    if args.text is None:
        args.text = sys.stdin.read()

    result = args.func(args)

    if result:
        print("success")
    else:
        print("failed")

    return int(not result)

if __name__ == '__main__':
    sys.exit(main())
