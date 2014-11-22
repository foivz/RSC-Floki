import datetime
import hashlib
import dose
import uuid
from mongokit import Document
from app.DAO import mongo, configParser

__author__ = 'Luka Strizic'


class Institution:
    def __init__(self, document):
        assert(isinstance(document, InstitutionDocument))
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

    def setCity(self, city, save=False):
        self.document['city'] = str(city)
        if(save): self.save()
        return

    def setAddress(self, address, save=False):
        self.document['address'] = str(address)
        if(save): self.save()
        return

    def setName(self, name, save=False):
        self.document['name'] = str(name)
        if(save): self.save()
        return

    def activate(self, save = False):
        self.document['active'] = True
        if(save): self.save()
        return

    def deactivate(self, save = False):
        self.document['active'] = False
        if(save): self.save()
        return

    def setAplusLow(self, low, save = False):
        self.document['A+low'] = low
        if(save): self.save()
        return

    def setAminusLow(self, low, save = False):
        self.document['A-low'] = low
        if(save): self.save()
        return

    def setBplusLow(self, low, save = False):
        self.document['B+low'] = low
        if(save): self.save()
        return

    def setBminusLow(self, low, save = False):
        self.document['B-low'] = low
        if(save): self.save()
        return

    def setABplusLow(self, low, save = False):
        self.document['AB+low'] = low
        if(save): self.save()
        return

    def setABminusLow(self, low, save = False):
        self.document['AB-low'] = low
        if(save): self.save()
        return

    def set0plusLow(self, low, save = False):
        self.document['0+low'] = low
        if(save): self.save()
        return

    def set0minusLow(self, low, save = False):
        self.document['0-low'] = low
        if(save): self.save()
        return

    def getAplus(self):
        return mongo.DoseDocument.find({'id' : self.document.id,
                                        'AB0' : 'A', 'Rh' : '+',
                                        'status' : 'available'}).count()

    def getAminus(self):
        return mongo.DoseDocument.find({'id' : self.document.id,
                                        'AB0' : 'A',
                                        'Rh' : '-',
                                        'status' : 'available'}).count()

    def getBplus(self):
        return mongo.DoseDocument.find({'id' : self.document.id,
                                        'AB0' : 'B',
                                        'Rh' : '+',
                                        'status' : 'available'}).count()

    def getBminus(self):
        return mongo.DoseDocument.find({'id' : self.document.id,
                                        'AB0' : 'B',
                                        'Rh' : '-',
                                        'status' : 'available'}).count()

    def getABplus(self):
        return mongo.DoseDocument.find({'id' : self.document.id,
                                        'AB0' : 'AB',
                                        'Rh' : '+',
                                        'status' : 'available'}).count()

    def getABminus(self):
        return mongo.DoseDocument.find({'id' : self.document.id,
                                        'AB0' : 'AB',
                                        'Rh' : '-',
                                        'status' : 'available'}).count()

    def get0plus(self):
        return mongo.DoseDocument.find({'id' : self.document.id,
                                        'AB0' : '0',
                                        'Rh' : '+',
                                        'status' : 'available'}).count()

    def get0minus(self):
        return mongo.DoseDocument.find({'id' : self.document.id,
                                        'AB0' : '0',
                                        'Rh' : '-',
                                        'status' : 'available'}).count()

def get_by_id(id):
    doc = mongo.InstitutionDocument.find_one({'id':id})
    if (doc):
        return Institution(doc)
    return None

def get_all_institutions_cursor():
    return mongo.InstitutionDocument.find()

@mongo.register
class InstitutionDocument(Document):
    __database__ = configParser.get("Mongo","DBname")
    __collection__ = 'institutions'

    use_schemaless = True
    use_dot_notation = True

    structure = {
        'city' : basestring,
        'address' : basestring,
        'name' : basestring,
        'id' : basestring,
        'A+low' : float,
        'A-low' : float,
        'B+low' : float,
        'B-low' : float,
        'AB+low' : float,
        'AB-low' : float,
        '0+low' : float,
        '0-low' : float,
        'active' : bool
    }

    default_values = {
        'id' : uuid.uuid4,
        'A+low' : 0.0,
        'A-low' : 0.0,
        'B+low' : 0.0,
        'B-low' : 0.0,
        'AB+low' : 0.0,
        'AB-low' : 0.0,
        '0+low' : 0.0,
        '0-low' : 0.0,
        'active' : False
    }
