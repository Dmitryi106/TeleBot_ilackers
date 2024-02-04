from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6911956163:AAEHbnfX9lO78oBGqTOZwWJI0oSUx66e2Lk"


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот запущен!')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<em>Привет! это �� бот для работы с ботом Telegram!</em>', parse_mode="HTML")


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAELUPNlv7TGs7hjfIryoDtVWNjLE1Dw1QACCAADwDZPE29sJgveGptpNAQ')
    await message.delete()


@dp.message_handler()
async def send_emogi(message: types.Message):
    await message.reply(message.text + "❤️")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)