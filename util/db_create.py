import sqlite3
DB_FILE = "app.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.execute("CREATE TABLE users (username TEXT, password TEXT)")
c.execute("CREATE TABLE posts (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, body TEXT)")


c.execute("INSERT INTO users VALUES(?, ?);", ('raday', 'test'))
c.execute("INSERT INTO users VALUES(?, ?);", ('jasch', 'lead'))
c.execute("INSERT INTO users VALUES(?, ?);", ('ibelkebir', 'whomst'))

#c.execute("INSERT INTO sessions VALUES(?, ?, ?);", ('raday', 'sesh1'))
#c.execute("INSERT INTO sessions VALUES(?, ?, ?);", ('jasch', 'sesh2'))
#c.execute("INSERT INTO sessions VALUES(?, ?, ?);", ('ibelkebir', 'sesh3'))

c.execute("INSERT INTO posts VALUES(?, ?, ?);", (None, 'raday', 'Hey, this is text'))
c.execute("INSERT INTO posts VALUES(?, ?, ?);", (None, 'jasch', 'asch'))
c.execute("INSERT INTO posts VALUES(?, ?, ?);", (None, 'ibelkebir', 'imad'))

db.commit()
db.close()
