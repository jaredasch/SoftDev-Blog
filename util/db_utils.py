from flask import flash, session
from os import urandom
from datetime import datetime
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
        #For testing, should flash username and password
        #flash(user)
        #flash(user[1])
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
    if (text != None):
        c.execute("INSERT INTO posts VALUES (?, ?, ?, ?)", [None, session.get("user"), text, datetime.now()])
    else:
        flash("No input for post")
    db.commit()
    db.close()


def get_posts(username):
    db = sqlite3.connect(DB_FILE)
    db.text_factory = str
    c = db.cursor()
    posts = c.execute("SELECT * FROM posts WHERE posts.username == ?", [username]).fetchall()
    db.close()
    return posts


def get_post(id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    post = c.execute("SELECT * FROM posts WHERE posts.id == ?" , [id]).fetchone()
    db.close()
    return post


def edit_post(post_id, text):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE posts SET body == ? WHERE posts.id == ?", [text, post_id])
    db.commit()
    db.close()


def get_all_posts():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM posts").fetchall()
    db.commit()
    db.close()
    return data
