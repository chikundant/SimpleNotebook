from abc import abstractmethod, ABC
from mysql.connector import connect, Error

import config


class DBModel(ABC):
    @abstractmethod
    def get_by_field(self, select, subj, comp):
        pass

    @abstractmethod
    def insert_field(self, *args):
        pass


class MySQLUser(DBModel):
    def get_by_field(self, select, subj, comp):
        try:
            with connect(
                host=config.HOST,
                user=config.USER,
                password=config.PASSWORD,
                database="notebook",
                auth_plugin='mysql_native_password'
            ) as conn:
                select_query = "SELECT {} FROM `user` WHERE `{}` = '{}'"
                with conn.cursor() as cursor:
                    cursor.execute(select_query.format(select, subj, comp))
                    res = cursor.fetchone()
                    if not res:
                        return None

                    return res
        except Error as e:
            print(e)

    def insert_field(self, *args):
        try:
            with connect(
                host=config.HOST,
                user=config.USER,
                password=config.PASSWORD,
                database="notebook",
                auth_plugin='mysql_native_password'
            ) as conn:
                select_query = "INSERT INTO `user` (username, email, password_hash) VALUES ('{}', '{}', '{}')"
                with conn.cursor() as cursor:
                    cursor.execute(select_query.format(args[0], args[1], args[2]))
                    conn.commit()
        except Error as e:
            print(e)


class MySQLNotes(DBModel):
    def get_by_field(self, select, subj, comp):
        try:
            with connect(
                host=config.HOST,
                user=config.USER,
                password=config.PASSWORD,
                database="notebook",
                auth_plugin='mysql_native_password'
            ) as conn:
                select_query = "SELECT {} FROM `note` WHERE `{}` = '{}' ORDER BY time DESC"
                with conn.cursor() as cursor:
                    cursor.execute(select_query.format(select, subj, comp))
                    res = cursor.fetchall()
                    if not res:
                        return None

                    return res
        except Error as e:
            print(e)

    def insert_field(self, *args):
        try:
            with connect(
                    host=config.HOST,
                    user=config.USER,
                    password=config.PASSWORD,
                    database="notebook",
                    auth_plugin='mysql_native_password'
            ) as conn:
                select_query = "INSERT INTO `note` (user_id, title, body) VALUES ('{}', '{}', '{}')"
                with conn.cursor() as cursor:
                    cursor.execute(select_query.format(args[0], args[1], args[2]))
                    conn.commit()
        except Error as e:
            print(e)

    def delete_field(self, id):
        try:
            with connect(
                    host=config.HOST,
                    user=config.USER,
                    password=config.PASSWORD,
                    database="notebook",
                    auth_plugin='mysql_native_password'
            ) as conn:
                delete_query = "DELETE FROM note WHERE id = {}"
                with conn.cursor() as cursor:
                    cursor.execute(delete_query.format(id))
                    conn.commit()
        except Error as e:
            print(e)

    def update_field(self, id, title, body):
        try:
            with connect(
                    host=config.HOST,
                    user=config.USER,
                    password=config.PASSWORD,
                    database="notebook",
                    auth_plugin='mysql_native_password'
            ) as conn:
                update_query = "UPDATE `note` SET time = CURRENT_TIMESTAMP(), title = '{}', body = '{}' WHERE id = {}"
                with conn.cursor() as cursor:
                    cursor.execute(update_query.format(title, body, id))
                    conn.commit()
        except Error as e:
            print(e)

    def find_field_by_one_definition(self, definition, id, value):
        try:
            with connect(
                    host=config.HOST,
                    user=config.USER,
                    password=config.PASSWORD,
                    database="notebook",
                    auth_plugin='mysql_native_password'
            ) as conn:
                find_query = "SELECT * FROM note WHERE user_id = {} AND {} LIKE '%{}%' ORDER BY title DESC"
                with conn.cursor() as cursor:
                    cursor.execute(find_query.format(id, definition, value))
                    res = cursor.fetchall()
                    if not res:
                        return None

                    return res
        except Error as e:
            print(e)

    def find_field_by_two_definitions(self, id, value1, value2):
        try:
            with connect(
                    host=config.HOST,
                    user=config.USER,
                    password=config.PASSWORD,
                    database="notebook",
                    auth_plugin='mysql_native_password'
            ) as conn:
                find_query = "SELECT * FROM note WHERE user_id = {} AND time LIKE '%{}%' AND title LIKE '%{}%' ORDER BY time DESC"
                with conn.cursor() as cursor:
                    cursor.execute(find_query.format(id, value1, value2))
                    res = cursor.fetchall()
                    if not res:
                        return None

                    return res
        except Error as e:
            print(e)
