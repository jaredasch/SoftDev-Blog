import sqlite3
import hashlib

DB_FILE = "app.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

defPass="hello".encode('utf-8')
hash_obj= hashlib.md5(defPass)
hashpass=hash_obj.hexdigest()

'''Default users'''
c.execute("INSERT INTO users VALUES(?, ?);", ('raday', hashpass))
c.execute("INSERT INTO users VALUES(?, ?);", ('jasch', hashpass))
c.execute("INSERT INTO users VALUES(?, ?);", ('ibelkebir', hashpass))

#VERY IMPORTANT-- HASHED PASSWORDS are 'hello', not the ones you had yesterday

db.commit()
db.close()
