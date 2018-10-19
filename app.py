from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3
import hashlib, datetime
#password = 'pa$$w0rd'
#h = hashlib.md5(password.encode())
#print(h.hexdigest())

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("landing_site.html")
#Need to figure out how to pick newest blogs with all info relevant

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html", title = "Sign Up")
    else:
        username = request.form.get("username")

        if(len(username) < 5):
            flash("Username must be 5 characters or longer")
            return redirect(url_for("signup"))
        elif(len(c.execute("SELECT * FROM users WHERE users.username == ?", username))>0):
            #if statement has syntax issues; incomplete
            flash("User already exists");
            return redirect(url_for("signup"))

        password = request.form.get("password")
        #Password criteria to be listed
        if (len(password)<8):
            flash("Password must be 8 characters or longer")
            return redirect(url_for("signup"))
        elif " " in password:
            flash("Password must not contain spaces")
            return redirect(url_for("signup"))

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", title = "Login")
    else:
        username = request.form.get("username")


@app.route("/post", methods = ["GET", "POST"])
def post():
    if request.method == "GET":
        return render_template("post.html")
    else:
        username = request.form.get("username")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        return render_template("edit.html")
    else:
        username = request.form.get("username")
        timestamp = request.form.get(times)
        new_timestamp = now.isoformat()
        post = request.form.get("posts")

if __name__ == "__main__":
    app.debug = True
    app.run()
