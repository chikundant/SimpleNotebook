from abc import abstractmethod, ABC
from mysql.connector import connect, Error


class DBModel(ABC):
    @abstractmethod
    def get_by_field(self, select, table, subj, comp):
        pass

    @abstractmethod
    def insert_field(self, table, *args):
        pass


class MySQL(DBModel):
    def get_by_field(self, select, table, subj, comp):
        try:
            with connect(
                host='localhost',
                user='chikunda',
                password='D52292023290',
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
                host='localhost',
                user='chikunda',
                password='D52292023290',
                database="notebook"
            ) as conn:
                select_query = "INSERT INTO `{}` (username, email, password_hash) VALUES ('{}', '{}', '{}')"
                with conn.cursor() as cursor:
                    cursor.execute(select_query.format(table, args[0], args[1], args[2]))
                    conn.commit()
        except Error as e:
            print(e)