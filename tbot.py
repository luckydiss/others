import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode
from async_scrapper import get_orders_database
import asyncio

import re


# создаем соединение с базой данных


# создаем объект бота
bot = Bot(token='5365165769:AAG3BuOXpFpp8KBywtuxkwdXBFP4OMZIYrE')
dp = Dispatcher(bot)

# функция для получения последних 5 заявок из базы данных
def get_last_orders():
    get_orders_database()
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    query = "SELECT * FROM orders ORDER BY id DESC LIMIT 5"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

from typing import List

import pymorphy2


def lemmatize_word(word: str) -> str:
    morph = pymorphy2.MorphAnalyzer()
    word_forms = morph.parse(word)[0].lexeme
    return word_forms


def filter_orders(orders: List, filter_words: List[str]) -> List:
    result = []
    splited_words = [word for phrase in filter_words for word in phrase.split()]

    for order in orders:
        order_id, topic, description, author = order
        order_text = f"{topic} {description}".lower()

        # лемматизируем каждое слово в заказе
        lemmatized_order = [lemmatize_word(word) for word in order_text.split()]

        lemmatized_words = [word.word for sublist in lemmatized_order for word in sublist]

        # проверяем, есть ли в заказе хотя бы одно ключевое слово из списка
        if any(word in splited_words for word in lemmatized_words):
            result.append(order)

    return list(set(result))

# функция для обработки запроса на начало работы с ботом
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # отправляем приветственное сообщение
    await message.reply("Привет! Я бот для получения информации о заказах.")

# функция для обработки запроса на получение последних заявок
@dp.message_handler(commands=['last_orders'])
async def send_last_orders(message: types.Message):
    while True:
        # получаем последние 5 заявок
        orders = get_last_orders()
        # создаем сообщение с информацией о заявках

        for order in orders:
            response = "<b>Последние заявки:</b>\n\n"
            order_id, topic, description, author = order

            # filter_words = ['питон', 'искусственный интеллект']
            filter_words =  ['питон', 'пайтон', 'python', 'jupyter', 'machine learning',
                             'машинное обучение', 'нейронная сеть', 'искусственный интеллект',
                             'pytorch', 'tensorflow', 'регрессия', 'паскаль', 'pascal',
                             'логином', 'loginom', 'deductor studio', 'дедуктор'
                             'матлаб', 'матлабе', 'matlab']

            filtered_orders = filter_orders(orders, filter_words)

            if filtered_orders:
                response += f"<b>Заявка №{order_id}</b>\n"
                response += f"<b>Тема:</b> {topic}\n"
                # удаляем HTML-теги из текста сообщения
                description = re.sub('<[^<]+?>', '', description)
                # разбиваем описание на части, чтобы оно помещалось в одно сообщение
                response_parts = [description[i:i+4096] for i in range(0, len(description), 4096)]
                for part in response_parts:
                    response += f"<b>Описание:</b> {part}\n"
                response += f"<b>Автор:</b> {author}\n\n"
                # отправляем сообщение пользователю
                await bot.send_message(chat_id=message.chat.id, text=response, parse_mode=ParseMode.HTML)
        # Пауза на 5 минут
        print('Пауза')
        await asyncio.sleep(300)

if __name__ == '__main__':
    executor.start_polling(dp)

