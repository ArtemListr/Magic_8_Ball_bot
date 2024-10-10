from configs import bot_token,name_dir
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
import random

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = bot_token

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


list_of_answers = ['Бесспорно','Предрешено','Никаких сомнений','Определённо да','Можешь быть уверен в этом','Мне кажется - да',
                   'Вероятнее всего','Хорошие перспективы','Знаки говорят - да',
                   'Да','Пока неясно, попробуй снова','Спроси позже','Лучше не рассказывать',
                   'Сейчас нельзя предсказать','Сконцентрируйся и спроси опять','Даже не думай','Мой ответ - нет',
                   'По моим данным - нет','Перспективы не очень хорошие','Весьма сомнительно']


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer(f'Привет,{message.from_user.first_name}!\nМеня зовут бот "Магический шар"!\nЗадай мне вопрос')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Задай мне вопрос, который тебя волнует'
        'я пришлю тебе мое предсказание'
    )

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"

async def send_sticker_echo(message: Message):
    await message.answer_sticker(message.sticker.file_id)
    await message.answer(text = message.sticker.file_id)


async def send_answer(message: Message):
    if '?' == message.text[-1] and type(message) == str:
        await message.reply(text=random.choice(list_of_answers))
    else:
        await message.answer_sticker('CAACAgIAAxkBAANCZwgEZE26qwSt3uB1avXdTgPBaCIAAjBAAAJFQ2FISYFHvDheLzA2BA')
        await message.answer(text = 'я отвечаю только на вопросы :)')

# Этот хэндлер будет срабатывать на отправку стикеров

dp.message.register(process_start_command,Command(commands=["start"]))
dp.message.register(process_help_command,Command(commands=['help']))
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_answer)

if __name__ == '__main__':
    dp.run_polling(bot)