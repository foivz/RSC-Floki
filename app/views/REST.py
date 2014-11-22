from flask import jsonify
from app import app

__author__ = 'Davor Obilinovic'


@app.route("/REST/test/")
def rest_test():
    return jsonify(status="OK",info={"disi":"frane"})
