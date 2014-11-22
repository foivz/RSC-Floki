from flask import request, redirect
from flask.ext.login import login_required
from app import app
from app.DAO import user as userClass, institution as institutionClass
from app.core import Functions

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
    inst = institution.get_by_id(id)
    inst.setName(data["name"])
    inst.setCountry(data["country"])
    inst.setCity(data["city"])
    inst.setAddress(data["address"])
    inst.setAplusLow(data["A+low"])
    inst.setAminusLow(data["A-low"])
    inst.setBplusLow(data["B+low"])
    inst.setBminusLow(data["B-low"])
    inst.setABplusLow(data["AB+low"])
    inst.setABminusLow(data["AB-low"])
    inst.set0plusLow(data["0+low"])
    inst.set0minusLow(data["0-low"])
    if data["active"]: inst.activate()
    else: inst.deactivate()
    inst.save()

    return redirect('/super/admin/editInstitution/%s' % id)
