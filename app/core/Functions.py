import uuid
from app.DAO import configParser, mongo

__author__ = 'Davor Obilinovic'


def push_registration_request(req):
    req["id"] = uuid.uuid4()
    mongo[configParser.get("Mongo","DBname")].registration_requests.insert(req)


def pull_registration_requests(type):
    cur =  mongo[configParser.get("Mongo","DBname")].registration_requests.find({"type":type})
    ret = []
    for obj in cur:
        ret.append(obj)
    return ret

def get_request_by_id(id):
    return  mongo[configParser.get("Mongo","DBname")].registration_requests.find_one({"id":id})