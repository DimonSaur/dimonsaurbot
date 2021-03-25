from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
      await bot.send_message(message.from_user.id, 'Привет! Связь со мной:\nTelegram: @dimonsaur\nVK: https://vk.com/dimonsaur',
                             reply_markup=kb.greet_kb)


@dp.message_handler()
async def process_reply(message: types.Message):
      await message.reply('Мой сервер в Minecraft:\nhttps://hardserver.ml')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)