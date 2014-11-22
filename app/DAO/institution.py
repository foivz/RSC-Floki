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

    def setCountry(self, country, save=False):
        self.document['country'] = str(country)
        if(save): self.save()
        return

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

    def warning(self):
        ret =  self.getAplus() <= self.document['A+low'] or \
                self.getAminus() <= self.document['A-low'] or \
                self.getBplus() <= self.document['B+low'] or \
                self.getBminus() <= self.document['B-low'] or \
                self.getABplus() <= self.document['AB+low'] or \
                self.getABminus() <= self.document['AB-low'] or \
                self.get0plus() <= self.document['0+low'] or \
                self.get0minus() <= self.document['0-low']
        return ret

def create_institution_from_request(req):
    doc = mongo.InstitutionDocument()
    doc['name'] = req['name']
    doc['city'] = req['city']
    doc['address'] = req['address']
    doc['country'] = req['country']
    return Institution(doc)

def get_by_id(id):
    doc = mongo.InstitutionDocument.find_one({'id':id})
    if (doc):
        return Institution(doc)
    return None

def get_all_institutions_cursor():
    return mongo.InstitutionDocument.find()

def get_all_institutions_array():
    ret =[]
    for inst in get_all_institutions_cursor():
        ret.append(Institution(inst))
    return ret

def uuidStr():
    return str(uuid.uuid4())

@mongo.register
class InstitutionDocument(Document):
    __database__ = configParser.get("Mongo","DBname")
    __collection__ = 'institutions'

    use_schemaless = True
    use_dot_notation = True

    structure = {
        'country' : basestring,
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
        'id' : uuidStr,
        'A+low' : 1.0,
        'A-low' : 1.0,
        'B+low' : 1.0,
        'B-low' : 1.0,
        'AB+low' : 1.0,
        'AB-low' : 1.0,
        '0+low' : 1.0,
        '0-low' : 1.0,
        'active' : True
    }
