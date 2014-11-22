from flask import request, render_template
from flask.ext.login import login_required, logout_user, login_user
from werkzeug.utils import redirect
from app import app
from app.DAO import user

__author__ = 'Davor Obilinovic'

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/login",methods=["GET","POST"])
def login_Page():
    if request.method == "POST":
        useName = request.form["username"]
        password = request.form["password"]
        u = user.get_by_username(useName)
        if u and u.check_password(password):
            login_user(u)
            return redirect("/")
    return render_template('login.html')

@app.route("/register/<type>", methods=["POST","GET"])
def register(type):
    return render_template("register.html")
