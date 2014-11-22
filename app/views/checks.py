from flask import request, jsonify
from app import app
from app.DAO import user as userClass

__author__ = 'Davor Obilinovic'


@app.route("/chack/username/exist")
def check_username_exist():
    data = request.args
    username = data["username"]
    user = userClass.get_by_username(username)
    if user:
        return jsonify({"status":"Error", "message":"User already exist!"})
    else:
        return jsonify({"status":"OK", "message":"OK"})

