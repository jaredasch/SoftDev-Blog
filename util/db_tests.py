import sqlite3
DB_FILE = "app.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.execute("INSERT INTO users VALUES(?, ?);", ('raday', 'test'))
c.execute("INSERT INTO users VALUES(?, ?);", ('jasch', 'lead'))
c.execute("INSERT INTO users VALUES(?, ?);", ('ibelkebir', 'whomst'))

# c.execute("INSERT INTO posts VALUES(?, ?, ?, ?);", ('0', 'raday', 'Hey, this is text', '1220'))
# c.execute("INSERT INTO posts VALUES(?, ?, ?, ?);", ('1', 'jasch', 'asch', '1223'))
# c.execute("INSERT INTO posts VALUES(?, ?, ?, ?);", ('2', 'ibelkebir', 'imad', '1225'))

db.commit()
db.close()
