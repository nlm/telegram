Pushover
========

a simple pushover command-line client to send messages
you will need an account on pushover.net and an app token to use it

app token
---------

app token can be passed either by command-line argument (-T) or by exporting
the PUSHOVER_APP_TOKEN environment variable. you can create an app on your
pushover user console.

push a message
--------------

```
usage: pushover push [-h] -k TARGET_KEY -m MESSAGE [-d DEVICE] [-t TITLE]
                     [-u URL] [-U URL_TITLE] [-p {-2,-1,0,1,2}]
                     [-s {pushover,bike,bugle,cashregister,classical,cosmic,falling,gamelan,incoming,intermission,magic,mechanical,pianobar,siren,spacealarm,tugboat,alien,climb,persistent,echo,updown,none}]
                     [-r RETRY] [-e EXPIRE] [-c CALLBACK]

optional arguments:
  -h, --help            show this help message and exit
  -k TARGET_KEY, --target-key TARGET_KEY
                        the user/group key (not e-mail address) of your user
                        (or you), viewable when logged into our dashboard
                        (often referred to as USER_KEY in the documentation
                        and code examples)
  -m MESSAGE, --message MESSAGE
                        your message
  -d DEVICE, --device DEVICE
                        your user's device name to send the message directly
                        to that device, rather than all of the user's devices
                        (multiple devices may be separated by a comma)
  -t TITLE, --title TITLE
                        your message's title, otherwise your app's name is
                        used
  -u URL, --url URL     a supplementary URL to show with your message
  -U URL_TITLE, --url-title URL_TITLE
                        a title for your supplementary URL, otherwise just the
                        URL is shown
  -p {-2,-1,0,1,2}, --priority {-2,-1,0,1,2}
                        send as -2 to generate no notification/alert, -1 to
                        always send as a quiet notification, 1 to display as
                        high-priority and bypass the user's quiet hours, or 2
                        to also require confirmation from the user
  -s {pushover,bike,bugle,cashregister,classical,cosmic,falling,gamelan,incoming,intermission,magic,mechanical,pianobar,siren,spacealarm,tugboat,alien,climb,persistent,echo,updown,none}, --sound {pushover,bike,bugle,cashregister,classical,cosmic,falling,gamelan,incoming,intermission,magic,mechanical,pianobar,siren,spacealarm,tugboat,alien,climb,persistent,echo,updown,none}
                        the name of one of the sounds supported by device
                        clients to override the user's default sound choice
  -r RETRY, --retry RETRY
                        how often (in seconds) the Pushover servers will send
                        the same notification to the user
  -e EXPIRE, --expire EXPIRE
                        how many seconds your notification will continue to be
                        retried for (every retry seconds)
  -c CALLBACK, --callback CALLBACK
                        publicly-accessible URL that Pushover servers will
                        send a request to when the user has acknowledged your
                        notification
```

check a receipt
---------------

```
usage: pushover receipt [-h] -r RECEIPT_ID

optional arguments:
  -h, --help            show this help message and exit
  -r RECEIPT_ID, --receipt-id RECEIPT_ID
                        the receipt id to query
```
