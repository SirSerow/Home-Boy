import csv

from aiogram.types import Message, InputFile

from loader import dp, bot, config, _
from services.users import count_users, get_users

from picamera import PiCamera
from time import sleep
import traceback

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

@dp.message_handler(i18n_text='Take picture 📷', is_admin=True)
@dp.message_handler(commands=['take_picture'], is_admin=True)
async def _take_picture(message: Message):
    camera = PiCamera()
    path = "pictures"
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        #await message.answer(_('Dir created'))
    ##try:
        
    #except:
    #    await message.answer(_('Camera open: NOT ok'))
    #else:

    camera.start_preview()
    sleep(.5)
    try:
        camera.capture(f'{os.getcwd()}/pictures/latest_picture.jpg')
    except Exception as e:
        camera.stop_preview()
        camera.close()
        await message.answer(_(f'{traceback.format_exc()}'))
    else:
        camera.stop_preview()    
        camera.close()
        await message.reply_photo(open(f'{os.getcwd()}/pictures/latest_picture.jpg', 'rb'))
    #try:
    #    camera.start_preview()
    #    sleep(5)
    #    camera.capture('/pictures/latest_picture.jpg')
    #except:
    #    camera.stop_preview()
    #    camera.close()
    #    await message.answer(_('Picture taken: NOT ok'))
    #else:
    #    camera.stop_preview()
    #    camera.close()
    #    await message.answer(_('Picture taken: ok'))
    
@dp.message_handler(i18n_text='opencv_show_last', is_admin=True)
@dp.message_handler(commands=['opencv_show_last'], is_admin=True)
async def _opencv_show_last(message: Message):
    path = "opencv"
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    await message.reply_photo(open(f'{os.getcwd()}/opencv/last_frame.jpg', 'rb'))

@dp.message_handler(i18n_text='opencv_show_last_movement', is_admin=True)
@dp.message_handler(commands=['opencv_show_last_movement'], is_admin=True)
async def _opencv_show_last_movement(message: Message):
    path = "opencv"
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    await message.reply_photo(open(f'{os.getcwd()}/opencv/last_motion_detected.jpg', 'rb'))
