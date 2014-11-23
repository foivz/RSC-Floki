from flask import request, redirect, jsonify
from flask.ext.login import login_required, current_user
from app import app
from app.DAO import user as userClass, institution as institutionClass, mongo
from app.core import Functions
import requests
from gcm import GCM

__author__ = 'Luka Strizic'

@login_required
@app.route("/super/admin/approveRequestCallback", methods=["POST"])
def approve_registration_request():
    data = request.form
    id = data["id"]
    req = Functions.get_request_by_id(id)

    doc = None
    if req['type'] == 'worker':
        doc = userClass.create_from_request(req)
    elif req['type'] == 'institution':
        doc = institutionClass.create_institution_from_request(req)

    doc.save()
    Functions.remove_request_by_id(id)

    return redirect('/super/admin/registrationRequests')

@login_required
@app.route("/institution/<id>/update", methods=["POST"])
def update_institution(id):
    data = request.form
    inst = institutionClass.get_by_id(id)
    inst.setName(data["name"])
    inst.setCountry(data["country"])
    inst.setCity(data["city"])
    inst.setAddress(data["address"])
    inst.setAplusLow(float(data["A+low"]))
    inst.setAminusLow(float(data["A-low"]))
    inst.setBplusLow(float(data["B+low"]))
    inst.setBminusLow(float(data["B-low"]))
    inst.setABplusLow(float(data["AB+low"]))
    inst.setABminusLow(float(data["AB-low"]))
    inst.set0plusLow(float(data["0+low"]))
    inst.set0minusLow(float(data["0-low"]))
    inst.save()
    return redirect('/super/admin/editInstitutions/%s' % id)

@login_required
@app.route("/institution/<id>/activate", methods=["POST"])
def activate_institution(id):
    inst = institutionClass.get_by_id(id)
    inst.activate()
    inst.save()

    return jsonify()

@login_required
@app.route("/institution/<id>/deactivate", methods=["POST"])
def deactivate_institution(id):
    inst = institutionClass.get_by_id(id)
    inst.deactivate()
    inst.save()
    return jsonify()

@login_required
@app.route("/worker/<username>/update", methods=["POST"])
def update_worker(username):
    data = request.form
    worker = userClass.get_by_username(username)
    worker.setUsername(data["username"])
    worker.setName(data["name"])
    worker.setSurname(data["surname"])
    worker.setCountry(data["country"])
    worker.setCity(data["city"])
    worker.setAddress(data["address"])
    worker.setAB0(data["AB0"])
    worker.setRh(data["Rh"])
    worker.setAccountType(data["type"])
    worker.save()
    return redirect('/super/admin/editWorkers/%s' % data["username"])

@login_required
@app.route("/donor/<username>/update", methods=["POST"])
def update_donor(username):
    data = request.form
    worker = userClass.get_by_username(username)
    worker.setUsername(data["username"])
    worker.setName(data["name"])
    worker.setSurname(data["surname"])
    worker.setCountry(data["country"])
    worker.setCity(data["city"])
    worker.setAddress(data["address"])
    worker.setAB0(data["AB0"])
    worker.setRh(data["Rh"])
    worker.save()
    return redirect('/super/admin/editDonors/%s' % data["username"])

@login_required
@app.route("/sendNotification", methods=["POST"])
def notify():
    data = request.form
    AB0 = data['AB0']
    Rh = data['Rh']
    country = data['country']
    city = data['city']
    address = data['address']
    message = data['message']
    donors = userClass.get_eligible_donors_array(AB0, Rh, country, city)
    if not message: message = generateMessage(AB0, Rh, city, address)
    gcm = GCM('AIzaSyBK9OhEEvws_AFT47BA5fqsiUBHX1Oi6XQ')
    r = requests.get("http://maps.googleapis.com/maps/api/geocode/json?address=" + country + " " + city + " " + address)
    r = r.json()['results'][0]['geometry']['location']
    lat = r['lat']
    lng = r['lng']
    for donor in donors:
        if donor['token']:
            gcm.plaintext_request(donor['token'], {'message':message, 'lat':str(lat), 'lng':str(lng)})
    return redirect('/')

def generateMessage(AB0, Rh, city, address):
    if AB0:
        return "Your blood type is " + AB0 + Rh + " and we would like You to donate some of your blood, because supplies are running low. \
        You can donate in " + city + " on address " + address + ". Thank You!"
    return "blood supplies are running low in " + city + " and we would like You to donate. You can do it at " + address + ". Thank you!"

@app.route("/setBloodType/<username>", methods=["POST"])
def set_blood_type(username):
    blod_type =request.form["bloodType"]
    RH = "-" if "-" in blod_type else "+"
    AB0 = blod_type.rstrip('-').rstrip('+')
    user = userClass.get_by_username(username)
    user.document["AB0"]= AB0
    user.document["RH"] = RH
    user.save()
    return redirect("/events/donations/%s"%username)

@login_required
@app.route("/event/donation/<username>",methods=["POST"])
def do_donation(username):
    user = userClass.get_by_username(username)
    data = request.form
    institutionId = current_user['institution']
    doc = mongo.EventDocument()
    doc['institutionID'] = institutionId
    doc['username'] = username
    doc["type"] = "donation"
    info = {}
    for key in data.keys():
        if key in ["tatoo","pierce"] :
            info[key] = True
        else:
            info[key] = data[key]
    doc["info"] = info
    doc.save()
    dose = mongo.DoseDocument()
    dose["institutionID"] = institutionId
    dose["AB0"] = user["AB0"]
    dose["RH"] = user["RH"]
    dose["donationId"] = doc["id"]
    dose.save()
    return redirect("/")
