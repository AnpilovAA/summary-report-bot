from sqlite3 import connect
from os import getenv


def db(func_db):
    db = getenv("DB")

    def connect_db(*args, **kwargs):
        print(args, kwargs)
        con = connect(db)
        active_cursor = con.cursor()
        func_db(args[0], args[1], active_cursor)

    return connect_db
