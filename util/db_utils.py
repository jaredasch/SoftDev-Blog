from flask import flash, session
from os import urandom
from datetime import datetime
import sqlite3
import hashlib
DB_FILE = "app.db"


'''Used to check if user exists with create_user,
reports back int to see if given user has data '''

def count_users(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    data = c.execute("SELECT * FROM users WHERE users.username == ?", [username]).fetchall()
    db.close()
    return len(data)

def create_user(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    ''' Checks if data corresponding to given username is found '''
    if get_user(username):
        flash("User already exists")
        return False
    elif len(username) < 5:
        flash("Username must be at least 5 characters")
        return False
    elif len(password) < 5:
        flash("Password must be at least 5 characters")
        return False
    hash_obj = hashlib.md5(password)
    hashpass = hash_obj.hexdigest()
    ''' If username and password meet length specifications, add name and pass combo to table '''
    c.execute("INSERT INTO users VALUES (?, ?)", [username, hashpass])
    db.commit()
    db.close()
    return True

def login_user(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    user = get_user(username)
    ''' Checks if no data can be found on given username '''
    if user == None:
        flash("User does not exist")
        db.close()
        return None
    elif user[1] != password:
        flash("Password is incorrect")
        db.close()
        return None
    ''' Set current session user '''
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
    '''If statement prevents empty posts from being spammed'''
    if (text != ''):
        ''' ID is automatically assigned in ascending order for each post '''
        c.execute("INSERT INTO posts VALUES (?, ?, ?, ?)", [None, session.get("user"), text, datetime.now()])
    else:
        flash("No input for post")
    db.commit()
    db.close()


def get_posts(username):
    db = sqlite3.connect(DB_FILE)
    db.text_factory = str
    c = db.cursor()
    ''' Get post based on username '''
    posts = c.execute("SELECT * FROM posts WHERE posts.username == ?", [username]).fetchall()
    db.close()
    return posts


def get_post(id):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    ''' Get post based on ID '''
    post = c.execute("SELECT * FROM posts WHERE posts.id == ?" , [id]).fetchone()
    db.close()
    return post


def edit_post(post_id, text):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    ''' Find corresponding post using ID and update its text '''
    c.execute("UPDATE posts SET body == ? WHERE posts.id == ?", [text, post_id])
    db.commit()
    db.close()


def get_all_posts():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    ''' Gets all posts created '''
    data = c.execute("SELECT * FROM posts").fetchall()
    db.commit()
    db.close()
    return data
