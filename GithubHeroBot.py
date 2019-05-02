"""Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot."""

from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
CHOOSING = range(1)
reply_keyboard = [['1', '2'],
                  ['3', '4'],
                  ['5']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def start(bot, update):
    update.message.reply_text("Hi type 1 2 3 or 4 for more", reply_markup=markup)
    return CHOOSING


def choice_1(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('reply1')
    return CHOOSING


def choice_2(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('reply2')
    return CHOOSING


def choice_3(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('reply3')
    return CHOOSING


def choice_4(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text('reply4')
    return CHOOSING


def done(bot, update, user_data):
    print("done")
    update.message.reply_text("conversation ended, i will stop")
    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("754353087:AAHRnA8fIIUT7FamQ0TRtLBDFcfqoOxSbqE")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            CHOOSING: [RegexHandler('1$',
                                    choice_1,
                                    pass_user_data=True),
                       RegexHandler('2$',
                                    choice_2,
                                    pass_user_data=True),
                       RegexHandler('3$',
                                    choice_3,
                                    pass_user_data=True),
                       RegexHandler('4$',
                                    choice_4,
                                    pass_user_data=True),
                       ],
        },

        fallbacks=[RegexHandler('5$', done, pass_user_data=True)],
        allow_reentry=True
    )

    dp.add_handler(conv_handler)

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
