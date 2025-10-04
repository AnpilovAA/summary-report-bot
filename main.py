from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters)
from dotenv import load_dotenv


from os import getenv
from db.create_db import create_db


from chat_wiretapping.audiotion_chats import audition
from handlers.start import start


def main():
    load_dotenv()
    token = getenv("TOKEN")
    db = getenv("DB")
    create_db(db)

    app = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler("start", start)

    audition_handler = MessageHandler(filters.TEXT, audition)

    app.add_handlers(
        [
            start_handler,
            audition_handler,
        ]
    )

    app.run_polling()


if __name__ == "__main__":
    main()
