import datetime
import hashlib
from flask import jsonify
from mongokit import Document
from app.DAO import mongo, configParser
from app.DAO.event import Event

__author__ = 'Davor Obilinovic'


class User:
    def __init__(self, document):
        assert(isinstance(document, UserDocument))
        self.document = document

    def __getitem__(self, item):
        ret = None
        try:
            ret = self.document[str(item)]
        except:
            pass
        return ret

    def save(self):
        self.document.save()

    def is_authenticated(self):
        return self.document!=None

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.document["username"]

    def get_username(self):
        return self.get_id()

    def profilePictureUrl(self):
        try:
            return "http://graph.facebook.com/"+self.document["facebook_name"]+"/picture?type=large"
        except:
            return "http://cdn.wallwuzz.com/uploads/2013/08/Anonymous-wallpaper.jpg"

    def check_password(self, password):
        m = hashlib.sha1()
        m.update(password)
        digest =  m.hexdigest()
        return digest == self.document["password"]

    def isWorker(self):
        return self.document['type'] in ['worker', 'admin', 'superadmin']

    def isAdmin(self):
        return self.document['type'] in ['admin', 'superadmin']

    def isSuperAdmin(self):
        return self.document['type'] == 'superadmin'

    def getDonations(self):
        cur = mongo.EventDocument.find({"type":"donation", "user":self.get_username()})
        donations = []
        for obj in cur:
            donations.append(Event(obj))
        return donations

    def getNumDonations(self):
        return len(self.getDonations())

    def getProfileJson(self):
        json = {}
        json["numDonations"] = self.getNumDonations()
        json["achivements"] = self.getAchivements()
        json["bloodType"] = {"AB0":self["AB0"],"RH":self["RH"]}
        json["country"] = self["country"]
        return json

    def getAchivements(self):
        return  ["prva donacija", "nesto drugo","TODO this"]


def get_by_username(username):
    doc = mongo.UserDocument.find_one({'username':username})
    if (doc):
        return User(doc)
    return None

def create_from_request(req):
    doc = mongo.UserDocument()
    doc['username'] = req['username']
    passwordHash = hashlib.sha1(req['password']).hexdigest()
    doc['password'] = passwordHash
    doc['type'] = req['type']
    doc['name'] = req['name']
    doc['surname'] = req['surname']
    doc['city'] = req['city']
    doc['address'] = req['address']
    doc['institutionID'] = req['institutionID']
    doc['country'] = req['country']
    return doc

@mongo.register
class UserDocument(Document):
    __database__ = configParser.get("Mongo","DBname")
    __collection__ = 'users'

    use_schemaless = True
    use_dot_notation = True

    structure = {
        'username' : basestring,
        'password' : basestring,
        'country'  : basestring,
        'type' : basestring,
        'name' : basestring,
        'surname' : basestring,
        'city' : basestring,
        'address' : basestring,
        'AB0' : basestring,
        'RH' : basestring
    }

    default_values = {
        'AB0': None,
        'RH': None
    }
