from sqlite3 import connect


from decorator_db import db


def create_db(db_name: str):
    con = connect(db_name)
    active_cursor = con.cursor()
    active_cursor.execute(
        "CREATE TABLE IF NOT EXISTS notebook(chat_id TEXT, message TEXT)"
    )


def read_db(db):
    con = connect(db)
    active_cursor = con.cursor()
    result = active_cursor.execute("SELECT name FROM sqlite_master")
    print(result.fetchall())


@db
def write_to_db(id: str, message: str, active_cursor: object):
    result = active_cursor.execute(
        f"INSER INTO notebook (chat_id, message) VALUES({id}, {message})"
        )
    result.fetchone()


if __name__ == "__main__":
    create_db("chats_messages.db")
    # write_to_db("231", "проверка")
    read_db("chats_messages.db")
