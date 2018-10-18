from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup", title = "Sign Up")
    else:
        username = request.form.get("username");

        if(len(username) < 5):
            flash("Username must be 5 characters or longer")
            return redirect(url_for("signup"))
        elif(len(c.execute("SELECT * FROM users WHERE users.username == ?", username) != 0):
            flash("User already exists");
            return redirect(url_for("signup"))

        pass = request.form.get("password")

@app.route("/post", methods = ["GET", "POST"])
def post():
    if request.method == "GET":
        return render_template("post.html")

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

if __name__ = "__main__":
    app.debug = True
    app.run()
