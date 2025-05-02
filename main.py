from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor



API_TOKEN = ''


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я эхо-бот. Напиши мне что-нибудь!")


@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo_message(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)