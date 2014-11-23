import datetime
import uuid
import random
from  app.DAO import institution as insClass, mongo

__author__ = 'Davor Obilinovic'

ABOs = ["A","B","0","AB"]
rhs = ["+","-"]
ins_ids = []
for ins in insClass.get_all_institutions_array():
    ins_ids.append(ins["id"])

ins = []
for i in range(400):
    r_AB0 = ABOs[random.randint(0,3)]
    r_rh = rhs[random.randint(0,1)]
    d = {
        "status" : "available",
        "institutionID" : ins_ids[random.randint(0,len(ins_ids)-1)],
        "dateCreated" : datetime.datetime.utcnow(),
        "AB0" : r_AB0,
        "donationId" : None,
        "RH" : r_rh,
        "id" : str(uuid.uuid4())
    }
    ins.append(d)

mongo["Floki"].doses.insert(ins)
