from __future__ import absolute_import, print_function
import os
import sys
import requests
from argparse import ArgumentParser
from .__init__ import Pushover

def do_push(args):
    pushover = Pushover(args.pushover_app_token)
    return pushover.send_message(args.target_key,
                                 args.message,
                                 title=args.title,
                                 url=args.url,
                                 url_title=args.url_title,
                                 priority=args.priority,
                                 retry=args.retry,
                                 expire=args.expire,
                                 callback=args.callback)

def do_receipt(args):
    pushover = Pushover(args.pushover_app_token)
    return pushover.get_receipt(args.receipt_id)

def main():
    parser = ArgumentParser()

    parser.add_argument('-T', '--pushover-app-token',
                        metavar='PUSHOVER_APP_TOKEN',
                        help=("your application's API token. "
                              "Can be defined in environment var "
                              "PUSHOVER_APP_TOKEN"),
                        default=os.environ.get('PUSHOVER_APP_TOKEN'))

    parser.add_argument('-f', '--format',
                        choices=('text', 'json'),
                        default='text',
                        help="program output format")

    subparsers = parser.add_subparsers()
    subparsers.required=True

    push_p = subparsers.add_parser('push')
    push_p.set_defaults(func=do_push)

    push_p.add_argument('-k', '--target-key',
                        required=True,
                        help=("the user/group key (not e-mail address) of "
                              "your user (or you), viewable when logged into "
                              " our dashboard (often referred to as USER_KEY "
                              "in the documentation and code examples)"))

    push_p.add_argument('-m', '--message',
                        help="your message")

    push_p.add_argument('-d', '--device',
                        help=("your user's device name to send the message "
                              "directly to that device, rather than all of "
                              "the user's devices (multiple devices may be "
                              "separated by a comma)"))

    push_p.add_argument('-t', '--title',
                        help=("your message's title, otherwise "
                              "your app's name is used"))

    push_p.add_argument('-u', '--url',
                        help="a supplementary URL to show with your message")

    push_p.add_argument('-U', '--url-title',
                        help=("a title for your supplementary URL, otherwise "
                              "just the URL is shown"))

    push_p.add_argument('-p', '--priority', type=int,
                        choices=(-2, -1, 0, 1, 2), default=0,
                        help=("send as -2 to generate no notification/alert, "
                              "-1 to always send as a quiet notification, "
                              "1 to display as high-priority and bypass the "
                              "user's quiet hours, or 2 to also require "
                              "confirmation from the user"))

    push_p.add_argument('-s', '--sound',
                        choices=Pushover.sounds,
                        help=("the name of one of the sounds supported by "
                              "device clients to override the user's "
                              "default sound choice"))

    push_p.add_argument('-r', '--retry',
                        default=60,
                        type=int,
                        help=("how often (in seconds) the Pushover servers "
                              "will send the same notification to the user"))

    push_p.add_argument('-e', '--expire',
                        default=300,
                        type=int,
                        help=("how many seconds your notification will "
                              "continue to be retried for "
                              "(every retry seconds)"))

    push_p.add_argument('-c', '--callback',
                        help=("publicly-accessible URL that Pushover servers "
                              "will send a request to when the user has "
                              "acknowledged your notification"))

    rece_p = subparsers.add_parser('receipt')
    rece_p.set_defaults(func=do_receipt)

    rece_p.add_argument('-r', '--receipt-id',
                        required=True,
                        help="the receipt id to query")

    args = parser.parse_args()

    requests.packages.urllib3.disable_warnings()

    if args.pushover_app_token is None:
        parser.error('PUSHOVER_APP_TOKEN is required')

    if args.message is None:
        args.message = sys.stdin.read()

    result = args.func(args)

    if args.format == 'json':
        print(result.json)
    else:
        print(result.text)

    return int(not result.is_success)

if __name__ == '__main__':
    sys.exit(main())
