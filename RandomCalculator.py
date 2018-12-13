# Token = 754353087:AAHRnA8fIIUT7FamQ0TRtLBDFcfqoOxSbqE
# installare libreria python-telegram-bot


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import telegram
import random

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = "754353087:AAHRnA8fIIUT7FamQ0TRtLBDFcfqoOxSbqE"

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    kb = [[telegram.KeyboardButton('/add')],
          [telegram.KeyboardButton('/sub')],
          [telegram.KeyboardButton('/mul')],
          [telegram.KeyboardButton('/div')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Welcome in GithubHeroBot",
                     reply_markup=kb_markup)
    update.message.reply_text('Benvenuto in GithubHeroBot')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help! dont ask me help')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    print(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def add(bot, update):
    """Comando1"""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    string = str(a) + "+" + str(b) + "=" + str(a+b)
    update.message.reply_text(string)

def sub(bot, update):
    """Comando2"""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    string = str(a) + "-" + str(b) + "=" + str(a - b)
    update.message.reply_text(string)

def mul(bot, update):
    """Comando3"""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    string = str(a) + "*" + str(b) + "=" + str(a * b)
    update.message.reply_text(string)

def div(bot, update):
    """Comando4"""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    try:
        string = str(a) + "/" + str(b) + "=" + str(a / b)
        update.message.reply_text(string)
    except ZeroDivisionError:
        update.message.reply_text("div by zero")


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("add", add))
    dp.add_handler(CommandHandler("sub", sub))
    dp.add_handler(CommandHandler("div", div))
    dp.add_handler(CommandHandler("mul", mul))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()