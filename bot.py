import os
import telebot
from telebot import types

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    menu_principal(message)


def menu_principal(message):
    markup = types.InlineKeyboardMarkup()

    markup.add(
        types.InlineKeyboardButton("📚 Produits numériques", callback_data="produits"),
        types.InlineKeyboardButton("🤖 Services IA", callback_data="services")
    )

    markup.add(
        types.InlineKeyboardButton("🛍️ Bons plans", callback_data="bonsplans"),
        types.InlineKeyboardButton("🎁 Offres gratuites", callback_data="gratuit")
    )

    markup.add(
        types.InlineKeyboardButton("💰 Mon compte", callback_data="compte")
    )

    bot.send_message(
        message.chat.id,
        "👋 Bienvenue sur GagneMalinFrance !\n\n"
        "💰 Découvre nos offres et services.\n\n"
        "Choisis une catégorie ci-dessous :",
        reply_markup=markup
    )


@bot.message_handler(commands=["menu"])
def menu(message):
    menu_principal(message)


@bot.callback_query_handler(func=lambda call: True)
def boutons(call):

    if call.data == "produits":
        texte = (
            "📚 PRODUITS NUMÉRIQUES\n\n"
            "Découvre nos produits numériques disponibles."
        )

    elif call.data == "services":
        texte = (
            "🤖 SERVICES IA\n\n"
            "Découvre nos services réalisés avec l'intelligence artificielle."
        )

    elif call.data == "bonsplans":
        texte = (
            "🛍️ BONS PLANS\n\n"
            "Retrouve ici nos bons plans et recommandations."
        )

    elif call.data == "gratuit":
        texte = (
            "🎁 OFFRES GRATUITES\n\n"
            "Retrouve ici les offres gratuites disponibles."
        )

    elif call.data == "compte":
        texte = (
            "💰 MON COMPTE\n\n"
            "Cette partie sera configurée prochainement."
        )

    else:
        texte = "❌ Option inconnue."

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, texte)


@bot.message_handler(func=lambda message: True)
def answer(message):
    bot.send_message(
        message.chat.id,
        "🤖 Utilise /menu pour afficher le menu."
    )


bot.infinity_polling()