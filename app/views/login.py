from flask import request, render_template
from flask.ext.login import login_required, logout_user, login_user
from werkzeug.utils import redirect
from app import app
from app.DAO import user, mongo
from app.core import Functions

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
    return render_template('login/login.html')

@app.route("/<type>/register", methods=["POST","GET"])
def register_institution(type):
    if request.method == "POST":
        data = request.form
        registration_request = {
            'type' : type,
            'name' : data["name"],
            'city' : data["city"],
            'address' : data["address"]
        }
        if type == "worker":
            registration_request["institution"] = data["institution"]
        Functions.push_registration_request(registration_request)
    institutions = None
    # if type == "worker":
    #     institutions = institution.get_all_institutions()
    return render_template("login/register.html")
