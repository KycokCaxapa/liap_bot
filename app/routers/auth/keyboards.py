from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

'''Использовать только reply-клавиатуру,
чтобы иметь возможность получать данные обратно в бота'''

app = WebAppInfo(url='https://suai.ru')
keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Web app',
                                                         web_app=app)]],
                               resize_keyboard=True)
