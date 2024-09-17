import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="736nbESY8Kmuw_Wl4")
# Диспетчер
dp = Dispatcher()


# Гендлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')



@dp.message()
async def all_message(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
