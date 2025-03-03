"""Скрипт для заполнения данными таблиц в БД Postgres."""
from csv import DictReader

import psycopg2

connect = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='1313'
)

with open(file='../homework-1/north_data/customers_data.csv', encoding='utf-8') as f:
    file_reader = DictReader(f)
    curs = connect.cursor()
    for info in file_reader:
        curs.execute('INSERT INTO customers VALUES (%s,%s,%s)', (info["customer_id"], info["company_name"], info["contact_name"]))
    connect.commit()
    curs.close()

with open(file='../homework-1/north_data/employees_data.csv', encoding='utf-8') as f:
    file_reader = DictReader(f)
    curs = connect.cursor()
    for info in file_reader:
        curs.execute('INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s)', (info["employee_id"], info["first_name"], info["last_name"], info['title'], info['birth_date'], info['notes']))
    connect.commit()
    curs.close()

with open(file='../homework-1/north_data/orders_data.csv', encoding='utf-8') as f:
    file_reader = DictReader(f)
    curs = connect.cursor()
    for info in file_reader:
        curs.execute('INSERT INTO orders VALUES (%s,%s,%s,%s,%s)', (info["order_id"], info["customer_id"], info["employee_id"], info['order_date'], info['ship_city']))
    connect.commit()
    curs.close()

connect.close()

