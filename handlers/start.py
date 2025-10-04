from telegram.ext import Updater, ContextTypes


async def start(update: Updater, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="Здравствуйте начинаю конспектировать,\
        по комманде /summ подготвлю для вас отчёт",
    )
