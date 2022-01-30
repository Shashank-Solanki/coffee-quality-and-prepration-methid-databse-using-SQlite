import sqlite3

CREATE_BEANS_TABLE = "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, ratings INTEGER);"
INSERT_BEANS = "INSERT INTO beans(name,method,ratings) VALUES (?,?,?);"
GET_ALL_BEANS = "SELECT * FROM beans;"
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"



def connect():
    return sqlite3.connect("data.db")

def create_tables(conn):
    with conn:
        conn.execute(CREATE_BEANS_TABLE)


def add_beans(conn, name, method, ratings):
    with conn:
        conn.execute(INSERT_BEANS,(name, method, ratings ))

def get_all_beans(conn):
    with conn:
        return conn.execute(GET_ALL_BEANS).fetchall()


def get_beans_by_name(conn,name):
    with conn:
        return conn.execute(GET_BEANS_BY_NAME, (name,)).fetchall()
