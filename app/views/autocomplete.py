from flask import request, jsonify
from flask.ext.login import login_required
import re
from app import app
from app.DAO import mongo

__author__ = 'Davor Obilinovic'

@login_required
@app.route('/autocomplete/users', methods=["GET"])
def autocomplete_sugestions():
    text = request.args['query']
    regx = re.compile("^"+text, re.IGNORECASE)
    curName = mongo.UserDocument.find({'name': regx, 'type':"donor"})
    curSurname = mongo.UserDocument.find({'surname': regx, 'type':"donor"})
    res = []
    name_len = curName.count()
    surname_len = curSurname.count()
    obj = None
    for i in range(max(name_len,surname_len)):
        name = None
        try:
            obj = curName.next()
            name ="%s %s, %s"%(obj["name"],obj["surname"],obj["address"])
        except:
            pass
        if name:
            e = {'value':name,'data':obj['username']}
            res.append(e)
        surname = None
        try:
            obj = curSurname.next()
            surname ="%s %s, %s"%(obj["name"],obj["surname"],obj["address"])
        except:
            pass
        if surname:
            e = {'value':surname,'data':obj['username']}
            res.append(e)

        if len(res)==10: break
    return jsonify(suggestions=res)
