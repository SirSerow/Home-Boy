import csv

from aiogram.types import Message, InputFile

from loader import dp, bot, config, _
from services.users import count_users, get_users

from picamera import PiCamera
from time import sleep

import os

@dp.message_handler(i18n_text='Export users 📁', is_admin=True)
@dp.message_handler(commands=['export_users'], is_admin=True)
async def _export_users(message: Message):
    count = count_users()

    file_path = config.DIR / 'users.csv'
    with open(file_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(['id', 'name', 'username', 'language', 'created_at'])

        for user in get_users():
            writer.writerow([user.id, user.name, user.username, user.language, user.created_at])

    text_file = InputFile(file_path, filename='users.csv')
    await message.answer_document(text_file, caption=_('Total users: {count}').format(count=count))


@dp.message_handler(i18n_text='Count users 👥', is_admin=True)
@dp.message_handler(commands=['count_users'], is_admin=True)
async def _users_count(message: Message):
    count = count_users()

    await message.answer(_('Total users: {count}').format(count=count))


@dp.message_handler(i18n_text='Count active users 👥', is_admin=True)
@dp.message_handler(commands=['count_active_users'], is_admin=True)
async def _active_users_count(message: Message):
    users = get_users()

    count = 0
    for user in users:
        try:
            if await bot.send_chat_action(user.id, 'typing'):
                count += 1
        except Exception:
            pass

    await message.answer(_('Active users: {count}').format(count=count))
@dp.message_handler(commands=['take_picture'], is_admin=True)
async def _take_picture(message: Message):
    
    path = "pictures"
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        await message.answer(_('Dir created'))
    
    try:
        camera = PiCamera()
    except:
        await message.answer(_('Camera open: NOT ok'))
    else:
        try:
            camera.capture('/pictures/latest_picture.jpg')
        except:
            await message.answer(_('Picture taken: NOT ok'))
        else:
            camera.close()
            await message.answer(_('Picture taken: ok'))
    