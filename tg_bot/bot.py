import asyncio

from aiogram import Bot, Dispatcher, types, filters

TOKEN = "6227029117:AAH_hpycXzA1-QIXggh2COl99fcP1JAUJ70"


dp = Dispatcher()
filters.CommandStart

@dp.message(filters.CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(f'Hello, {message.from_user.full_name}')


@dp.message()
async def echo_handler(message: types.Message):
    try:
        await message.reply(message.text)
    except TypeError:
        await message.answer("Nice try!")


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())