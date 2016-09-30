Telegram
========

a simple telegram command-line client to send messages
you will need a bot on telegram to use it

bot token
---------

bot token can be passed either by command-line argument (-T) or by exporting
the TELEGRAM_BOT_TOKEN environment variable. you can create a bot on telegram

send a message
--------------

```
usage: telegram send_message [-h] -i CHAT_ID [-N DISABLE_NOTIFICATION]
                             [-t TEXT]

optional arguments:
  -h, --help            show this help message and exit
  -i CHAT_ID, --chat-id CHAT_ID
                        the chat id
  -N DISABLE_NOTIFICATION, --disable-notification DISABLE_NOTIFICATION
                        disable notification
  -t TEXT, --text TEXT  your text
```
