"""Создать таблицу продуктов. Атрибуты продукта:
id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id. """

import sqlite3

def create_table():
    with sqlite3.connect("homework11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                prise INTEGER,
                quantity INTEGER,
                comment VARCHAR
            );
            """
        )


def create_product(name: str, prise: int, quantity: int, comment: int):
    with sqlite3.connect("homework11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (name, prise, quantity, comment)
            VALUES (?, ?, ?, ?);
            """,
           (name, prise, quantity, comment),
        )
        session.commit()


def search_product(quere: str):
    with sqlite3.connect("homework11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE id = ?
            """,
            (quere,),
        )
        session.commit()
        return cursor.fetchall()


def ap_producr():
    with sqlite3.connect("homework11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE user 
            SET prise = 900
            WHERE id = 5
            """
        )
        session.commit()


def delete_producr():
    with sqlite3.connect("homework11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM user
            WHERE id = 10
            """

        )
        session.commit()


if __name__ == "__main__":
#    create_product('phone', 850, 3, 'honor')
#    ap_producr()
#    delete_producr()
    resuil = search_product(11)
    print(resuil)
