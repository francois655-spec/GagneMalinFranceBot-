import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "👋 Bienvenue sur GagneMalinFrance !\n\n"
        "💰 Découvre nos offres et services.\n"
        "🛍️ Produits numériques\n"
        "✍️ Services IA\n"
        "🎁 Offres gratuites\n\n"
        "Utilise /menu pour commencer."
    )

@bot.message_handler(commands=["menu"])
def menu(message):
    bot.reply_to(
        message,
        "📋 MENU\n\n"
        "📚 Produits numériques\n"
        "🤖 Services IA\n"
        "🛍️ Bons plans\n"
        "🎁 Offres gratuites\n"
        "💰 Mon compte"
    )

@bot.message_handler(func=lambda message: True)
def answer(message):
    bot.reply_to(
        message,
        "Je suis GagneMalinFrance 🤖\n"
        "Tape /menu pour voir les possibilités."
    )

bot.infinity_polling()