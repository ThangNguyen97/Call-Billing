import sqlite3

conn = sqlite3.connect('database.db', check_same_thread=False)


def insert_db(user_name, call_duration):
    cu = conn.cursor()
    cu.execute(f"INSERT INTO mobile values('{user_name}',{call_duration})")
    conn.commit()
    cu.close()


def get_db_by_user(user_name):
    cu = conn.cursor()
    cu.execute(f"SELECT * FROM mobile WHERE user_name='{user_name}'")
    data = cu.fetchall()
    conn.commit()
    cu.close()
    return data
