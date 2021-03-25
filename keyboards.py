from aiogram.types import ReplyKeyboardMarkup, \
                        KeyboardButton

# Одна кнопка
btnContacts = KeyboardButton("Проект")
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnContacts)