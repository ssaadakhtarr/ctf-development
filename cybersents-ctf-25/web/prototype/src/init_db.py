import sqlite3
import random

flag = "flag{b3ing_bl1nd_1s_t0ugh}"
flag_table = f"flag_table_{random.randbytes(5).hex()}"
flag_column = f"flag_column_{random.randbytes(5).hex()}"

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
c.execute("INSERT INTO users (username, password) VALUES ('guest', 'supersecret')")

c.execute('''CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
c.execute("INSERT INTO products (name, price) VALUES ('Laptop', 999.99)")
c.execute("INSERT INTO products (name, price) VALUES ('Phone', 499.99)")

c.execute(f'''CREATE TABLE {flag_table} (id INTEGER PRIMARY KEY, {flag_column} TEXT)''')
c.execute(f"INSERT INTO {flag_table} ({flag_column}) VALUES ('{flag}')")

conn.commit()
conn.close()

print("Database initialized with users, products, and flag_table.")
