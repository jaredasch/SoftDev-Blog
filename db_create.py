import sqlite3
DB_FILE = "app.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.execute("CREATE TABLE users (name TEXT, password BLOB)")
c.execute("CREATE TABLE sessions (username TEXT, session_key TEXT)")
c.execute("CREATE TABLE posts (id INTEGER, username TEXT, body TEXT, timestamp INTEGER)")

db.commit()
db.close()
