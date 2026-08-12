import os
import telebot
from telebot import types

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "menu"])
def menu_principal(message):
    clavier = types.InlineKeyboardMarkup()

    clavier.add(
        types.InlineKeyboardButton("📚 Produits numériques", callback_data="produits"),
        types.InlineKeyboardButton("🤖 Services IA", callback_data="services")
    )

    clavier.add(
        types.InlineKeyboardButton("🛍️ Bons plans", callback_data="bonsplans"),
        types.InlineKeyboardButton("🎁 Offres gratuites", callback_data="gratuit")
    )

    clavier.add(
        types.InlineKeyboardButton("💰 Mon compte", callback_data="compte")
    )

    bot.send_message(
        message.chat.id,
        "👋 Bienvenue sur GagneMalinFrance !\n\n"
        "💰 Découvre nos offres et services.\n\n"
        "👇 Choisis ce qui t'intéresse :",
        reply_markup=clavier
    )


@bot.callback_query_handler(func=lambda call: True)
def bouton_clique(call):

    if call.data == "produits":
        texte = "📚 PRODUITS NUMÉRIQUES\n\nNos ebooks et autres produits numériques seront bientôt disponibles."

    elif call.data == "services":
        texte = "🤖 SERVICES IA\n\nCV, lettres, textes et créations personnalisées seront bientôt disponibles."

    elif call.data == "bonsplans":
        texte = "🛍️ BONS PLANS\n\nNos bons plans seront bientôt disponibles."

    elif call.data == "gratuit":
        texte = "🎁 OFFRES GRATUITES\n\nNos offres gratuites seront bientôt disponibles."

    elif call.data == "compte":
        texte = "💰 MON COMPTE\n\nCette partie sera ajoutée prochainement."

    else:
        texte = "❌ Option inconnue."

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, texte)


@bot.message_handler(func=lambda message: True)
def autre_message(message):
    bot.send_message(
        message.chat.id,
        "🤖 Utilise /menu pour afficher le menu."
    )


bot.infinity_polling()