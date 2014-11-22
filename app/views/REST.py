from flask import jsonify, request
from app import app
from app.DAO import user as userClass, mongo
from app.DAO.user import User

__author__ = 'Davor Obilinovic'


@app.route("/REST/profile")
def rest_profile():
    usersCur = mongo.UserDocument.find(request.args)
    results = []
    for userObj in usersCur:
        user = User(userObj)
        results.append(user.getProfileJson())
    return jsonify(status="OK",results=results)

@app.route("/REST/login", methods=["POST"])
def login_donor():
    data = request.args
    username, password = data["username"],data["password"]
    userClass.get_by_username()
    pass

@app.route("/REST/test/")
def rest_test():
    return jsonify(status="OK",info={"disi":"frane"})

