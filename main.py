import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {
    "proxy_url": settings.PROXY_URL,
    "urllib3_proxy_kwargs": {
        "username": settings.USERNAME,
        "password": settings.PASSWORD,
    }
}

def greet_user(update, context):
    print("/start raised")
    update.message.reply_text("Hello user!")

def echo(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, echo))

    logging.info("The bot has been launched")
    mybot.start_polling()
    mybot.idle()
    
if __name__ == "__main__":
    main()
