import sqlite3
DB_FILE = "app.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()
'''Makes users and posts table'''
c.execute("CREATE TABLE users (username TEXT, password TEXT)")
c.execute("CREATE TABLE posts (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, body TEXT, time_stamp INTEGER)")

db.commit()
db.close()
