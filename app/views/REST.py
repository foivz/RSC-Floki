import hashlib
from flask import jsonify, request
from app import app
from app.DAO import user as userClass, mongo
from app.core import Functions
import simplejson as json

__author__ = 'Davor Obilinovic'


@app.route("/test/REST/login", methods=["POST"])
def strest_login_donor():
    return jsonify(args=request.args, data = request.data, form =request.form)

@app.route("/REST/donors")
def register_donor():
    try:
        data = request.args
        doc = mongo.UserDocumen()
        doc["username"] = data["username"]
        doc["password"] = hashlib.sha1(data["password"]).hexDigest()
        doc["AB0"] = data["AB0"] if "AB0" in data.keys() else None
        doc["RH"] = data["RH"] if "RH" in data.keys() else None
        doc["name"] = data["name"]
        doc["surname"] = data["surname"]
        doc["country"] = data["country"]
        doc["city"] = data["city"]

        doc.save()
        return jsonify(status="OK")
    except Exception as e:
        return jsonify(status=e.message)

@app.route("/REST/profile", methods=["GET","POST"])
def rest_profile():
    try:
        token = request.args["token"]
        username = Functions.get_username_from_token(token)
        user = userClass.get_by_username(username)
        if request.method == "POST":
            data = json.loads(request.args["data"])
            for key in data.keys():
                if not "token" in key:
                    user.document[key] = data[key]
            user.save()
            return jsonify(status="OK")
        return jsonify(status="OK",profile=user.getProfileJson())
    except Exception as e:
        return jsonify(status=e.message)

@app.route("/REST/login", methods=["POST"])
def login_donor():
    data = request.args
    username, password = data["username"],data["password"]
    user = userClass.get_by_username(username)
    if not user or not user.check_password(password):
        return jsonify(status="auth fail")
    token = Functions.create_session(user)
    return jsonify(status="OK", token=token)

@app.route("/REST/test/")
def rest_test():
    return jsonify(status="OK",info={"disi":"frane"})

@app.route("/REST/subscribe")
def rest_subscribe():
    token = request.args["token"]
    username = Functions.get_username_from_token(token)
    user = userClass.get_by_username(username)
    user.setNotificationToken(request.args["notificationToken"], True)
    return jsonify(status="OK")

@app.route("/REST/unsubscribe")
def rest_unsubscribe():
    token = request.args["token"]
    username = Functions.get_username_from_token(token)
    user = userClass.get_by_username(username)
    user.clearNotificationToken(True)
    return jsonify(status="OK")

@app.route("/REST/events")
def rest_push_event():
    token = request.args["token"]
    username = Functions.get_username_from_token(token)
    user = userClass.get_by_username(username)
    doc = mongo.EventDocument()
    doc["username"] = user.get_username()
    doc["institutionID"] = None
    doc["type"] = request.args["type"]
    doc["info"] = {}
    return jsonify(status="OK")
