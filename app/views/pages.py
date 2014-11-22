from flask import render_template
from flask.ext.login import login_required, current_user
from app import app
from  app.DAO import user as userClass

__author__ = 'Davor Obilinovic'

@app.route('/')
@login_required
def index():
    return render_template('index.html',
                           user=current_user)

@login_required
@app.route("/user/<username>/profile", methods=["GET"])
def user_profile(username):
    usr = userClass.get_by_username(username)
    return render_template("userProfile.html",
                           user = current_user,
                           editedUser = usr)

@login_required
@app.route("/events/donations/<username>", methods=["GET"])
def do_donatinon(username):
    donator = userClass.get_by_username(username)
    return render_template("userDonating.html",
                           donator = donator,
                           user = current_user)
