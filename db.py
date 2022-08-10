from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# import sqlite3
#
# connection = sqlite3.connect("data.db")
# cursor = connection.cursor()
#
# create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"  # by making id as INTEGER
#                 # we auto-increment it. So now no need to pass id in each insertion, it will  autofill it in the row.
# cursor.execute(create_table)
#
# create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real, store_id int)"
# cursor.execute(create_table)
#
# create_table = "CREATE TABLE IF NOT EXISTS stores (id INTEGER PRIMARY KEY, name text)"
# cursor.execute(create_table)
#
# connection.commit()
# connection.close()