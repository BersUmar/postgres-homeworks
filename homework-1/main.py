"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

connect = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='1313'
)
