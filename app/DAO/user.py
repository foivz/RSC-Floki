import datetime
import hashlib
import institution
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

    def setUsername(self, username, save=False):
        self.document['username'] = username
        if(save): self.save()
        return

    def setName(self, name, save=False):
        self.document['name'] = name
        if(save): self.save()
        return

    def setSurname(self, surname, save=False):
        self.document['surname'] = surname
        if(save): self.save()
        return

    def setCountry(self, country, save=False):
        self.document['country'] = country
        if(save): self.save()
        return

    def setCity(self, city, save=False):
        self.document['city'] = city
        if(save): self.save()
        return

    def setAddress(self, address, save=False):
        self.document['address'] = address
        if(save): self.save()
        return

    def setAB0(self, ab0, save=False):
        self.document['AB0'] = ab0
        if(save): self.save()
        return

    def setRh(self, rh, save=False):
        self.document['RH'] = rh
        if(save): self.save()
        return

    def setInstitutionID(self, id, save=False):
        self.document['institutionID'] = id
        if(save): self.save()
        return

    def setAccountType(self, type, save=False):
        self.document['type'] = type
        if(save): self.save()
        return

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
        return self.document['type'] in ['worker', 'admin', 'superadmin'] and self.document.has_key('institutionID') and self.document['institutionID']

    def isAdmin(self):
        return self.document['type'] in ['admin', 'superadmin']

    def isSuperAdmin(self):
        return self.document['type'] == 'superadmin'

    def getInstitutionNameCity(self):
        if not self.document.has_key('institutionID') : return ""
        inst = institution.get_by_id(self.document['institutionID'])
        return inst['name'] + "; " + inst['city']

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

    def setNotificationToken(self, token, save=False):
        self.document['token'] = token
        if save: self.save()
        return

    def clearNotificationToken(self, save=False):
        self.document['token'] = ''
        if save: self.save()
        return

    def nextDate(self):
        event = mongo.EventDocument.find({'username':donor['username']}).sort({'date':-1})[0]
        eventType = event['type']
        eventDate = event['date']
        sex = self.document['sex']
        if eventType == 'donation' and sex == 'M' and datetime.datetime.utcnow() < eventDate + datetime.timedelta(days=90):
            return eventDate + datetime.timedelta(days=90)
        if eventType == 'donation' and sex == 'F' and datetime.datetime.utcnow() < eventDate + datetime.timedelta(days=120):
            return eventDate + datetime.timedelta(days=120)
        if eventType == 'sickness' and datetime.datetime.utcnow() < eventDate + datetime.timedelta(days = '14') :
            return eventDate + datetime.timedelta(days = '14')
        if eventType == 'tatooOrPiercing' and datetime.datetime.utcnow() < eventDate + datetime.timedelta(days = '180'):
            return eventDate + datetime.timedelta(days = '180')
        return datetime.datetime.utcnow()

    def canDonate(self):
        return self.nextDate() == datetime.datetime.utcnow()

def get_by_username(username):
    doc = mongo.UserDocument.find_one({'username':username})
    if (doc):
        return User(doc)
    return None

def get_all_users_cursor():
    return mongo.UserDocument.find()

def get_all_workers_cursor():
    return mongo.UserDocument.find({'$or' : [{'type': 'worker'},{'type': 'admin'},{'type': 'superadmin'}]})

def get_all_donors_cursor():
    return mongo.UserDocument.find({'type': 'donor'})

def get_all_users_array():
    ret =[]
    for usr in get_all_users_cursor():
        ret.append(User(usr))
    return ret

def get_all_workers_array():
    ret =[]
    for usr in get_all_workers_cursor():
        ret.append(User(usr))
    return ret

def get_all_donors_array():
    ret =[]
    for usr in get_all_donors_cursor():
        ret.append(User(usr))
    return ret

def get_eligible_donors_array(AB0, Rh, country, city):
    ret = []
    tmp = []
    if not AB0:
        AB0 = ['A', 'B', 'AB', '0']
    if not Rh:
        Rh = ['+', '-']
    for donor in mongo.UserDocument.find({'type':'donor', 'country':country,'$in' : [{'AB0':AB0}, {'Rh': Rh}] }):
        ret.append(User(donor))
    if country:
        for donor in ret:
            if donor['country'] == country:
                tmp.append(donor)
        ret = tmp
        tmp = []
    if city:
        for donor in ret:
            if donor['city'] == city:
                tmp.append(donor)
        ret = tmp
        tmp = []
    for donor in ret:
        event = mongo.EventDocument.find({'username':donor['username']}).sort({'date':-1})[0]
        eventType = event['type']
        eventDate = event['date']
        sex = donor['sex']
        if eventType == 'donation' and sex == 'M' and datetime.datetime.utcnow() < eventDate + datetime.timedelta(days=90) or \
           eventType == 'donation' and sex == 'F' and datetime.datetime.utcnow() < eventDate + datetime.timedelta(days=120):
            pass
        elif eventType == 'sickness' and datetime.datetime.utcnow() < eventDate + datetime.timedelta(days = '14') :
            pass
        elif eventType == 'tatooOrPiercing' and datetime.datetime.utcnow() < eventDate + datetime.timedelta(days = '180'):
            pass
        else:
            tmp.append(donor)
    ret = tmp
    tmp = []
    return ret


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
