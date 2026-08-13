import os
import telebot
from telebot import types

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# Nom du fichier ebook
EBOOK_FILE = "Gagné malin France bot 50 idée gagner argent interné.pdf"


@bot.message_handler(commands=["start", "menu"])
def menu_principal(message):
    clavier = types.InlineKeyboardMarkup()

    clavier.add(
        types.InlineKeyboardButton(
            "📚 Produits numériques",
            callback_data="produits"
        ),
        types.InlineKeyboardButton(
            "🤖 Services IA",
            callback_data="services"
        )
    )

    clavier.add(
        types.InlineKeyboardButton(
            "🛍️ Bons plans",
            callback_data="bonsplans"
        ),
        types.InlineKeyboardButton(
            "🎁 Offres gratuites",
            callback_data="gratuit"
        )
    )

    clavier.add(
        types.InlineKeyboardButton(
            "💰 Mon compte",
            callback_data="compte"
        )
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
        clavier = types.InlineKeyboardMarkup()

        clavier.add(
            types.InlineKeyboardButton(
                "📕 50 idées pour gagner de l'argent",
                callback_data="ebook"
            )
        )

        bot.answer_callback_query(call.id)

        bot.send_message(
            call.message.chat.id,
            "📚 PRODUITS NUMÉRIQUES\n\n"
            "Découvre notre premier ebook :\n\n"
            "📕 50 idées pour gagner de l'argent sur Internet\n\n"
            "Clique ci-dessous pour continuer 👇",
            reply_markup=clavier
        )

    elif call.data == "ebook":
        bot.answer_callback_query(call.id)

        bot.send_message(
            call.message.chat.id,
            "📕 50 idées pour gagner de l'argent sur Internet\n\n"
            "💰 Prix : bientôt disponible\n\n"
            "Le paiement et l'envoi automatique de l'ebook "
            "seront ajoutés à l'étape suivante."
        )

    elif call.data == "services":
        texte = (
            "🤖 SERVICES IA\n\n"
            "CV, lettres, textes et créations personnalisées "
            "seront bientôt disponibles."
        )

        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, texte)

    elif call.data == "bonsplans":
        texte = (
            "🛍️ BONS PLANS\n\n"
            "Nos bons plans seront bientôt disponibles."
        )

        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, texte)

    elif call.data == "gratuit":
        texte = (
            "🎁 OFFRES GRATUITES\n\n"
            "Nos offres gratuites seront bientôt disponibles."
        )

        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, texte)

    elif call.data == "compte":
        texte = (
            "💰 MON COMPTE\n\n"
            "Cette partie sera ajoutée prochainement."
        )

        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, texte)

    else:
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "❌ Option inconnue."
        )


@bot.message_handler(func=lambda message: True)
def autre_message(message):
    bot.send_message(
        message.chat.id,
        "🤖 Utilise /menu pour afficher le menu."
    )


bot.infinity_polling()