import sqlite3
from sqlite3 import Error
from aiogram import types

from data import config


def search_mob(text):
    try:
        conn = sqlite3.connect(config.FileNameDataBase)
        sql_user = f"SELECT first_name, middle_name " \
                   f"FROM User " \
                   f"WHERE mobile_num LIKE '{text.strip('+')}'"
        cursor = conn.execute(sql_user)
        result = cursor.fetchall()
        if result:
            return result
        else:
            return False
    except Error as e:
        print(f"The error '{e}' occurred")


def search_user_on_id(text):
    try:
        connection = sqlite3.connect(config.FileNameDataBase)
        sql = f"select first_name, middle_name " \
              f"from User " \
              f"where user_id_in_telegram like '{text}'"
        cursor = connection.execute(sql)
        result = cursor.fetchall()
        if connection:
            cursor.close()
            connection.close()
    except Error as e:
        print(f"The error '{e}' occurred")
    return result


def getcategory():
    try:
        connection = sqlite3.connect(config.FileNameDataBase)
        sql = f"select * from items"
        cursor = connection.execute(sql)
        result = cursor.fetchall()
        if connection:
            cursor.close()
            connection.close()
    except ConnectionError as e:
        print(f"Error : {e}")
    return result


def user_add_in_database(mes: types.Message):
    pn = mes.contact.phone_number
    user_id = mes.contact.user_id
    if search_user_id(mes.from_user.id):
        pass
    else:
        try:
            connection = sqlite3.connect("db.db3")
            sql = f"update User set user_id_in_telegram = {user_id} where mobile_num ={pn.strip('+')}"
            connection.execute(sql)
            connection.commit()
            print("added!")
        except Error as e:
            print(f"The error '{e}' occurred")


def search_user_id(text):
    try:
        connection = sqlite3.connect("db.db3")
        sql = f"select user_id_in_telegram " \
              f"from User " \
              f"where user_id_in_telegram LIKE '{text}'"
        cursor = connection.execute(sql)
        result = cursor.fetchall()
        print(result)
    except Error as e:
        print(f"The error '{e}' occurred")
    if len(result):
        return True
    else:
        return False


def search_object(text):
    result = None
    try:
        print(text)
        result = None
        conn = sqlite3.connect("db.db3")
        sql = f"select o.ops, o.sks, o.skud, o.svik, o.svn, o.eo, o.ib " \
            f"from User " \
            f"inner join objects o on User.object = o.id " \
            f"where user_id_in_telegram like '{text}'"
        cur = conn.execute(sql)
        result = cur.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
    return result
