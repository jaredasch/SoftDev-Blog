import sqlite3
DB_FILE = "app.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()


'''Default users'''
c.execute("INSERT INTO users VALUES(?, ?);", ('raday', '5d41402abc4b2a76b9719d911017c592'))
c.execute("INSERT INTO users VALUES(?, ?);", ('jasch', '5d41402abc4b2a76b9719d911017c592'))
c.execute("INSERT INTO users VALUES(?, ?);", ('ibelkebir', '5d41402abc4b2a76b9719d911017c592'))

#VERY IMPORTANT-- HASHED PASSWORDS are 'hello', not the ones you had yesterday

# c.execute("INSERT INTO posts VALUES(?, ?, ?, ?);", ('0', 'raday', 'Hey, this is text', '2018-10-23 09:49:28.267347'))
# c.execute("INSERT INTO posts VALUES(?, ?, ?, ?);", ('1', 'jasch', 'asch', '2018-10-23 09:49:28.267347'))
# c.execute("INSERT INTO posts VALUES(?, ?, ?, ?);", ('2', 'ibelkebir', 'imad', '2018-10-23 09:49:28.267347'))

db.commit()
db.close()
