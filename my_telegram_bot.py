import os
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import my_chatbot
import translator


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = my_chatbot.conversation(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(response))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, world!")


def my_bot_instance():
    # Instância do bot do telegram
    bot = ApplicationBuilder().token(os.getenv('bot_token')).build()

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    bot.add_handler(start_handler)
    bot.add_handler(message_handler)

    bot.run_polling()

