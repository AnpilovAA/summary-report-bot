from telegram import Bot
from dotenv import load_dotenv


from os import getenv
from asyncio import run


async def main():
    load_dotenv()
    token = getenv("TOKEN")
    Bot(token)


if __name__ == "__main__":
    run(main())
