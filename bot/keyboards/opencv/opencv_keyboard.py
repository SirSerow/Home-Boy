from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from loader import _

def get_opencv_markup(user):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    if user.is_admin:
        markup.add(_('Last movement detected ❗️'))
        markup.add(_('Clean frame 🌅'))
        markup.add(_('Last face 🥷'))
        markup.add(_('Last frame 📹'))

    if len(markup.keyboard) < 1:
        return ReplyKeyboardRemove()
    
    return markup