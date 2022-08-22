from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client

from aiogram.types import ReplyKeyboardRemove



@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Сделайте выбор', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/https://t.me/cosmetics_produceb_bot')

@dp.message_handler(commands=['Сроки_доставки'])
async def cosmetic_time_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Может сегодня, а может и завтра=)\nВ зависимости от нагрузи, но не более 3 рабочих дней')



@dp.message_handler(commands=['Доставка'])
async def cosmetic_area_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Только Москва и  ближайшее подмосковье')

@dp.message_handler(commands=['Продукция'])
async def cosmetic_product_command(message : types.Message):
    for ret in cur_execute('SELECT * FROM product').fetchall():
        await bot.send_foto(message.from_user.id, ret[0], f'{ret[1]}\nЦена {ret[-1]}')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(cosmetic_area_command, commands=['Доставка'])
    dp.register_message_handler(cosmetic_time_command, commands=['Сроки_доставки'])
    dp.register_message_handler(cosmetic_product_command, commands=['Продукция'])






