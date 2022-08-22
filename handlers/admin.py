from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# Начало диалога загрузки нового пункта меню
@dp.message_handler(commands=['Загрузить'], state=None)
async def cm_start(message : types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузи фото')

# Первый ответ и пишем словарь
@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file.id
    await FSMAdmin.next()
    await message.reply('Теперь введи название')

# Второй ответ
@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введи описание')

# Третий ответ
@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь нужно указать цену')

# Крайний ответ   и используе полученные данные
@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))

    await state.finish

# Регистрируем хендлеры
def register_hendlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin)
    dp.register_message_handler(load_name, state=FSMAdmin)
    dp.register_message_handler(load_description, state=FSMAdmin)
    dp.register_message_handler(load_price, state=FSMAdmin)






