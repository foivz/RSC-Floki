from os import abort
from flask import jsonify, request
from app import app
from app.DAO import user as userClass, mongo
from app.DAO.user import User
from app.core import Functions

__author__ = 'Davor Obilinovic'


@app.route("/REST/profile")
def rest_profile():
    token = request.args["token"]
    username = Functions.get_username_from_token(token)
    user = userClass.get_by_username(username)
    return jsonify(status="OK",profile=user.getProfileJson())

@app.route("/REST/login", methods=["POST"])
def login_donor():
    data = request.args
    username, password = data["username"],data["password"]
    user = userClass.get_by_username(username)
    if not user.check_password(password):
        return jsonify(status="auth fail")
    token = Functions.create_session(user)
    return jsonify(status="OK", token=token)

@app.route("/REST/test/")
def rest_test():
    return jsonify(status="OK",info={"disi":"frane"})

