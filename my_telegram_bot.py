import os
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import re
from datetime import datetime
import my_chatbot
import translator


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = str(my_chatbot.conversation(update.message.text))

    # Formatando o nome
    response = re.sub(r'(?=Nome do filme: )', "\n\n", response)

    # Formatando a descrição
    response = re.sub(r'(?=Descrição: )', "\n\n", response)

    # Formatando a data
    response = re.sub(r'(?=Data de lançamento: )', "\n\n", response)
    try:
        old_date = response.split('Data de lançamento: ')[1]
        old_date = datetime.strptime(old_date, "%Y-%m-%d")
        response = response[:-10]
        response += old_date.strftime('%d/%m/%Y')
    except:
        pass

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


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

