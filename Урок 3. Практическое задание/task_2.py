"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""





import hashlib
from uuid import uuid4
import mysql.connector


def check_password(psswd: str):
    # Создаем соединение с нашей базой данных
    db_connect = mysql.connector.connect(user='root', database='test_database', password='Svetlanka!4')
    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = db_connect.cursor()

    # Генерируем "соль" и формируем Хэш первого пароля
    salt = uuid4().hex
    hash_obj_1 = hashlib.sha256(salt.encode() + psswd.encode())
    hash_1 = hash_obj_1.hexdigest()
    print(f'Хэш1: {hash_1}')

    # Записываем соль и хэш в БД. Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
    cursor.execute("INSERT INTO hashes (salt, hash) VALUES (%s, %s)", (salt, hash_1))
    # Проверка
    cursor.execute("SELECT hash FROM hashes ORDER BY id LIMIT 4")
    results = cursor.fetchall()
    print(f'В базе данных хранится строка: {results}')

    password_2 = input('Введите пароль еще раз для проверки: ')
    hash_obj_2 = hashlib.sha256(salt.encode() + password_2.encode())
    hash_2 = hash_obj_2.hexdigest()
    print(f'Хэш извлеченный из БД: {results[-1][-1]}')

    # Проверяем совпадают ли хеш первого пароля, записанный в БД и хеш второго пароля
    if results[-1][-1] == hash_2:
        print('Вы ввели ВЕРНЫЙ пароль')
    else:
        print('Вы ввели НЕВЕРНЫЙ пароль')

    # Закрываем соединение с БД
    db_connect.close()


password_1 = input('Введите пароль: ')
check_password(password_1)