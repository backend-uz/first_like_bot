from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import os

TOKEN=os.environ.get('TOKEN')

updater = Updater(TOKEN)
dp = updater.dispatcher

def start(update: Update, context:CallbackContext):
    bot = context.bot

    chat_id = update.message.chat.id

    btn1 = KeyboardButton(text="👍")
    btn2 = KeyboardButton(text="👎")

    keyboard = ReplyKeyboardMarkup([[btn1, btn2]], resize_keyboard=True)


    bot.sendMessage(chat_id, "LIKE and DISLIKE", reply_markup=keyboard)


dp.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()