from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_photo_inline_markup():
    markup = InlineKeyboardMarkup()

    markup.add(InlineKeyboardButton('Сделать фото', callback_data='photo'))

    return markup
