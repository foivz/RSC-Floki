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
