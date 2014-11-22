import datetime
import hashlib
from mongokit import Document
from app.DAO import mongo, configParser

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
        'country'  : basestring,
        'username' : basestring,
        'password' : basestring,
        'type' : basestring,
        'name' : basestring,
        'surname' : basestring,
        'city' : basestring,
        'address' : basestring,
    }
