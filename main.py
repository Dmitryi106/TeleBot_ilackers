from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6911956163:AAEHbnfX9lO78oBGqTOZwWJI0oSUx66e2Lk"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp)