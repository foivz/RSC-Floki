from flask import request, redirect
from flask.ext.login import login_required
from app import app
from app.core import Functions
import app.DAO.institution as institution
import app.DAO.user as user

__author__ = 'Luka Strizic'

@login_required
@app.route("/super/admin/approveRequestCallback", methods=["POST"])
def approve_registration_request():
    data = request.form
    id = data["id"]
    req = Functions.get_request_by_id(id)

    doc = None
    if req['type'] == 'worker':
        doc = user.UserDocument()
        doc['username'] = req['username']
        doc['password'] = req['password']
        doc['type'] = req['type']
        doc['name'] = req['name']
        doc['surname'] = req['surname']
        doc['city'] = req['city']
        doc['address'] = req['address']
        doc['institutionID'] = req['institutionID']
    elif req['type'] == 'institution':
        doc = institution.InstitutionDocument()
        doc['name'] = req['name']
        doc['city'] = req['city']
        doc['address'] = req['address']

    doc.save()
    Functions.remove_request_by_id(id)

    return redirect('/super/admin/registrationRequests')