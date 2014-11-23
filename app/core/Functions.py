import uuid
from app.DAO import configParser, mongo

__author__ = 'Davor Obilinovic'


def push_registration_request(req):
    req["id"] = str(uuid.uuid4())
    mongo[configParser.get("Mongo","DBname")].registration_requests.insert(req)


def pull_registration_requests(type):
    cur =  mongo[configParser.get("Mongo","DBname")].registration_requests.find({"type":type})
    ret = []
    for obj in cur:
        ret.append(obj)
    return ret

def get_request_by_id(id):
    return  mongo[configParser.get("Mongo","DBname")].registration_requests.find_one({"id":id})

def remove_request_by_id(id):
    return  mongo[configParser.get("Mongo","DBname")].registration_requests.remove({"id":id})

def create_session(user):
    token = str(uuid.uuid4())
    mongo[configParser.get("Mongo","DBname")].tokens.insert({"username":user.get_username(),"token":token})
    return token


def get_username_from_token(token):
    return mongo[configParser.get("Mongo","DBname")].tokens.find_one({"token":token})["username"]
