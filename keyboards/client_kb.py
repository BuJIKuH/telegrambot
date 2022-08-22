from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Сроки_доставки')
b2 = KeyboardButton('/Доставка')
b3 = KeyboardButton('/ПРОДУКЦИЯ')
b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Отправить где Я', request_location=True)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b3).add(b2).insert(b1).add(b4).insert(b5)
