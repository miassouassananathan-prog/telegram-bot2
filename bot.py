from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

# Récupère le token depuis les variables Railway
TOKEN = os.getenv("TOKEN")

# Ton lien à ajouter
LINK = "\n\n Rejoins-nous : https://t.me/toncanal"

# Fonction pour modifier la description
async def add_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post
    if not message:
        return

    # Vérifie si le lien est déjà présent
    if message.caption and "https://t.me/toncanal" in message.caption:
        return

    # Crée la nouvelle description
    if message.caption:
        new_caption = message.caption + LINK
    else:
        new_caption = LINK

    try:
        await message.edit_caption(new_caption)
    except Exception as e:
        print(f"Erreur lors de l'édition du message : {e}")

# Crée l'application et ajoute le handler
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ChatType.CHANNEL, add_link))

# Démarre le bot
app.run_polling()