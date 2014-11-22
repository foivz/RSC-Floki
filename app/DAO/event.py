from datetime import datetime
import uuid
from mongokit import Document
from app.DAO import mongo, configParser

__author__ = 'Luka Strizic'


class Event:
    def __init__(self, document):
        assert(isinstance(document, EventDocument))
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

    def setUsername(self, username, save=False):
        self.document['username'] = str(username)
        if(save): self.save()
        return

    def setWeight(self, weight, save=False):
        self.document['weight'] = weight
        if(save): self.save()
        return

    def setDonated(self, save=False):
        self.document['donated'] = True
        if(save): self.save()
        return

    def setNotDonated(self, save=False):
        self.document['donated'] = False
        if(save): self.save()
        return

    def setInstitutionID(self, id, save=False):
        self.document['institutionID'] = str(id)
        if(save): self.save()
        return


def get_by_id(id):
    doc = mongo.EventDocument.find_one({'id':id})
    if (doc):
        return Event(doc)
    return None

def uuidStr():
    return str(uuid.uuid4())

@mongo.register
class EventDocument(Document):
    __database__ = configParser.get("Mongo","DBname")
    __collection__ = 'events'

    use_schemaless = True
    use_dot_notation = True

    structure = {
        'id' : basestring,
        'username' : basestring,
        'institutionID' : basestring,
        'donated' : bool,
        'status' : basestring,
        'date' : datetime,
        'weight' : float,
    }

    default_values = {
        'status' : ' ',
        'date' : datetime.utcnow,
        'weight' : 0.0,
        'id' : uuidStr
    }
