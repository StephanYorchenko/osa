from telegram     import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Filters, MessageHandler, CallbackQueryHandler, Updater

class Buttons(Enum):
    Help = ""

class Color(Enum):
    red = 1
    green = 2
    blue = 3

MainMenuKeyboard = [[InlineKeyboardButton(text = "Начать игру", callback_data = "/startGame")],
                    [InlineKeyboardButton(text = "Помощь",      callback_data = "/help")],
                    [InlineKeyboardButton(text = "Статистика",  callback_data = "/statistics")]]


DefaultKeyboard = [[KeyboardButton(text = "Начать игру", callback_data = "/startGame")]]
DefaultKeyboard_ = [[InlineKeyboardButton(text = "Начать игру", callback_data = "/startGame")]]

class Upd:
    def __init__(self):
        pass


class Bot:
    def __init__(self, token):
        self.updater = Updater(token)

        self.updater.dispatcher.add_error_handler(self._Exc)

        self.updater.dispatcher.add_handler(CallbackQueryHandler(self._CallBackQueryHandler))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, self._MessageHandler))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.command, self._CommandHandler))

    def Run(self):
        self.updater.start_polling()

    def _CallBackQueryHandler(self, bot, update):
        print(update)

    def _CommandHandler(self, bot, update):
        args = update.message.text.split()

        print(bot)
        print(update)

        if(args[0] == "/start"):
            #update.message.reply_text("Хей, привет.", reply_markup = ReplyKeyboardMarkup(DefaultKeyboard, True, True))
            update.message.reply_text("Хей, привет.", reply_markup = InlineKeyboardMarkup(DefaultKeyboard_))


        elif args[0] == '/startGame':
            update.message.reply_text("WORK!!")
        else:
            self._Help(update)

    def _MessageHandler(self, bot, update):
        print(update)

    def _StartGame(self, player_id):
        pass

    def _Help(self, update):
        update.message.reply_text("Хз, тут должна быть помощь")

    def _Exc(self, bot, update, exc):
        print(exc)

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

with open('token', 'r', encoding='utf-8') as f:
    Bot(f.read()[:-1]).Run()
