from flask import flash, session
from os import urandom
import sqlite3
DB_FILE = "app.db"

def count_users(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM users WHERE users.username == ?", [username]).fetchall()
    db.close()
    return len(data)

def create_user(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if count_users(username) > 0:
        flash("User already exists")
        return False
    elif len(username) < 5:
        flash("Username must be at least 5 characters")
        return False
    elif len(password) < 5:
        flash("Password must be at least 5 characters")
        return False
    c.execute("INSERT INTO users VALUES (?, ?)", [username, password])
    db.commit()
    db.close()
    return True


def login_user(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    user = c.execute("SELECT * FROM users WHERE users.username == ?" , [username]).fetchone()
    if user == None:
        flash("User does not exist")
        db.close()
        return None
    elif user[1] != password:
        flash("Password is incorrect")
        db.close()
        return None
    session["user"] = username
    db.close()
    return True


def get_user(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    user = c.execute("SELECT * FROM users WHERE users.username == ?" , [username]).fetchone()
    db.close()
    return user


def insert_post(text):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO posts VALUES (?, ?, ?)", [None, session.get("user"), text])
    db.commit()
    db.close()

def get_posts(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    posts = c.execute("SELECT * FROM posts WHERE posts.username == ?", [username]).fetchall()
    db.close()
    return posts
