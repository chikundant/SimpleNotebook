from abc import abstractmethod, ABC
from mysql.connector import connect, Error

import config


class DBModel(ABC):
    @abstractmethod
    def get_by_field(self, select, table, subj, comp):
        pass

    @abstractmethod
    def insert_field(self, table, *args):
        pass


class MySQLUser(DBModel):
    def get_by_field(self, select, table, subj, comp):
        try:
            with connect(
                host=config.HOST,
                user=config.USER,
                password=config.PASSWORD,
                database="notebook"
            ) as conn:
                select_query = "SELECT {} FROM `{}` WHERE `{}` = '{}'"
                with conn.cursor() as cursor:
                    cursor.execute(select_query.format(select, table, subj, comp))
                    res = cursor.fetchone()
                    if not res:
                        return None

                    return res
        except Error as e:
            print(e)

    def insert_field(self, table, *args):
        try:
            with connect(
                host=config.HOST,
                user=config.USER,
                password=config.PASSWORD,
                database="notebook"
            ) as conn:
                select_query = "INSERT INTO `{}` (username, email, password_hash) VALUES ('{}', '{}', '{}')"
                with conn.cursor() as cursor:
                    cursor.execute(select_query.format(table, args[0], args[1], args[2]))
                    conn.commit()
        except Error as e:
            print(e)


class MySQLNotes(DBModel):
    def get_by_field(self, select, table, subj, comp):
        try:
            with connect(
                host=config.HOST,
                user=config.USER,
                password=config.PASSWORD,
                database="notebook"
            ) as conn:
                select_query = "SELECT {} FROM `{}` WHERE `{}` = '{}' ORDER BY time DESC"
                with conn.cursor() as cursor:
                    cursor.execute(select_query.format(select, table, subj, comp))
                    res = cursor.fetchall()
                    if not res:
                        return None

                    return res
        except Error as e:
            print(e)

    def insert_field(self, table, *args):
        try:
            with connect(
                    host=config.HOST,
                    user=config.USER,
                    password=config.PASSWORD,
                    database="notebook"
            ) as conn:
                select_query = "INSERT INTO `{}` (user_id, title, body) VALUES ('{}', '{}', '{}')"
                with conn.cursor() as cursor:
                    cursor.execute(select_query.format(table, args[0], args[1], args[2]))
                    conn.commit()
        except Error as e:
            print(e)

    def delete_field(self, table, id):
        try:
            with connect(
                    host=config.HOST,
                    user=config.USER,
                    password=config.PASSWORD,
                    database="notebook"
            ) as conn:
                delete_query = "DELETE FROM {} WHERE id = {}"
                with conn.cursor() as cursor:
                    cursor.execute(delete_query.format(table, id))
                    conn.commit()
        except Error as e:
            print(e)

    def update_field(self, table, id, title, body):
        try:
            with connect(
                    host=config.HOST,
                    user=config.USER,
                    password=config.PASSWORD,
                    database="notebook"
            ) as conn:
                update_query = "UPDATE `{}` SET time = CURRENT_TIMESTAMP(), title = '{}', body = '{}' WHERE id = {}"
                with conn.cursor() as cursor:
                    cursor.execute(update_query.format(table, title, body, id))
                    conn.commit()
        except Error as e:
            print(e)