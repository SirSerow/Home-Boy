from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from loader import _


def get_default_markup(user):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    markup.add(_('Help 🆘'), _('Settings 🛠'))

    if user.is_admin:
        markup.add(_('Export users 📁'))
        markup.add(_('Count users 👥'))
        markup.add(_('Count active users 👥'))
        #markup.add(_('Take picture 📷'))
        markup.add(_('Last frame 📹'),_('Last movement detected ❗️'), _('Clean frame 🌅'), _('Last face 🥷'))

    if len(markup.keyboard) < 1:
        return ReplyKeyboardRemove()

    return markup
