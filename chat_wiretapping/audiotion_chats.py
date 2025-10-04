from telegram.ext import Updater, ContextTypes


async def audition(update: Updater, context: ContextTypes.DEFAULT_TYPE):
    """Получаем id чата и сообщение"""
    chat = update.message.chat.id
    message = update.message.text
