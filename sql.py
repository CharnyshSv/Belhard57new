import psycopg2

#https://sqlitestudio.pl/

conn = psycopg2.connect("db.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE if NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
    );
""")

cur.execute("""
    CREATE TABLE if NOT EXISTS roles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
    );
""")
cur.execute("""
    CREATE TABLE if NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE NOT NULL,
    password TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id)
    );
""")

cur.execute("""
    CREATE TABLE if NOT EXISTS articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (user_id) REFERENCES users(id));
""")

conn.commit()