import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("TOKEN")
LINK = "\n\n Rejoins-nous : @hentai_sama_8"

def add_link(update, context):
    message = update.channel_post

    if message.caption:
        if "https://t.me/toncanal" in message.caption:
            return
        new_caption = message.caption + LINK
    else:
        new_caption = LINK

    try:
        message.edit_caption(new_caption)
    except:
        pass

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.chat_type.channel, add_link))

updater.start_polling()
updater.idle()