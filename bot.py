from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")
LINK = "\n\n🔗 Rejoins-nous : @sexe_industrie"

async def add_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post

    if message.caption:
        if "https://t.me/toncanal" in message.caption:
            return
        new_caption = message.caption + LINK
    else:
        new_caption = LINK

    try:
        await message.edit_caption(new_caption)
    except:
        pass

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ChatType.CHANNEL, add_link))
app.run_polling()