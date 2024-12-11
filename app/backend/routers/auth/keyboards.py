from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

'''Использовать только reply-клавиатуру,
чтобы иметь возможность получать данные обратно в бота'''

def keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    app = WebAppInfo(url='')
    keyboard.button(text='Открыть веб-приложение',
                    web_app=app)
    keyboard.adjust(1)
    return keyboard.as_markup()
