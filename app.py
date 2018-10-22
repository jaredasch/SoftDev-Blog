from flask import Flask, render_template, request, session, redirect, url_for, flash
from util.db_utils import count_users, create_user, login_user, get_user, insert_post, get_posts, edit_post, get_post
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("landing_site.html", current_user = session.get("user"))


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if "user" in session.keys():
        return redirect(url_for("index"))
    if request.method == "GET":
        return render_template("signup.html", title = "Sign Up", current_user = session.get("user"))
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        if create_user(username, password):
            login_user(username, password)
            return redirect(url_for("index"))
        return render_template("signup.html", title = "Sign Up", current_user = session.get("user"))


@app.route("/login", methods = ["GET", "POST"])
def login():
    if "user" in session.keys():
        return redirect(url_for("index"))
    if request.method == "GET":
        return render_template("login.html", title = "Login", current_user = session.get("user"))
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        login = login_user(username, password)
        if login == None:
            return render_template("login.html", title = "Login", current_user = session.get("user"))
        return redirect(url_for("index"))


@app.route("/logout", methods = ["GET"])
def logout():
    if "user" in session.keys():
        session.pop("user")
    return redirect(url_for("login"))


@app.route("/u/<username>", methods = ["GET"])
def profile(username):
    return render_template("profile.html", user = username, posts = get_posts(username), current_user = session.get("user"))


@app.route("/create_post", methods = ["POST"])
def create_post():
    insert_post(request.form.get("blog_post"))
    return redirect(request.referrer)


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    if request.method == "GET":
        post = get_post(post_id)
        if(post[1] != session.get("user")):
            return render_template("profile.html", user = post[1], posts = get_posts(get_post(post_id)[1]), current_user = session.get("user"))
        return render_template("profile.html", user = session.get("user"), current_user = session.get("user"), posts = get_posts(get_post(post_id)[1]), edit_id = post_id)
    
    post = get_post(post_id)
    if(post[1] != session.get("user")):
        return render_template("profile.html", user = post[1], posts = get_posts(get_post(post_id)[1]), current_user = session.get("user"))
    edit_post(post_id, request.form.get("blog_post"))
    return render_template("profile.html", user = post[1], posts = get_posts(get_post(post_id)[1]), current_user = session.get("user"))

if __name__ == "__main__":
    app.debug = True
    app.run()
