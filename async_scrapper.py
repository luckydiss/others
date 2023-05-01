import json
import sqlite3
import requests

def get_orders_database() -> sqlite3.Connection:
    # определяем схему таблицы
    create_table_query = """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER ,
            topic TEXT NOT NULL,
            description TEXT NOT NULL,
            author TEXT NOT NULL
        );
    """

    # открываем соединение с базой данных SQLite
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    # cursor.execute("DROP TABLE orders")

    # создаем таблицу, если она не существует
    cursor.execute(create_table_query)

    # читаем данные из JSON-файла и преобразуем их в формат, который можно использовать для выполнения запросов SQL
    url = "https://api.studwork.ru/orders?discipline_group_ids[]=4&my_disciplines=false&my_types=false"
    response = requests.get(url)
    json_data = response.json()

    orders_id = []
    for order in json_data['orders']:
        orders_id.append(order['id'])

    for order_id in orders_id:
        url = f"https://api.studwork.ru/orders/{order_id}"
        response = requests.get(url)
        order = response.json()
        print(order['order']['topic'])
        orders_to_insert = [(order['order']['id'], order['order']['topic'], order['order']['text'], order['order']['customer']['name'])]

        # выполняем INSERT-запросы для вставки данных в таблицу базы данных
        cursor.execute("""
                INSERT INTO orders (id, topic, description, author)
                SELECT ?, ?, ?, ?
                WHERE NOT EXISTS (
                    SELECT 1 FROM orders WHERE id = ?
                )
            """, orders_to_insert[0] + (order['order']['id'],))

        # сохраняем изменения в базе данных
        conn.commit()