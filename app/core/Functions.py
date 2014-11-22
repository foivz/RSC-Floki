import uuid
from app.DAO import configParser, mongo

__author__ = 'Davor Obilinovic'


def push_registration_request(req):
    req["id"] = uuid.uuid4()
    mongo[configParser.get("Mongo","DBname")].registration_requests.insert(req)