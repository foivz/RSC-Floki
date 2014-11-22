from flask import render_template, request
from flask.ext.login import current_user, login_required
from app import app
from app.core import Functions
import app.DAO.institution as institution
import app.DAO.user as user

__author__ = 'Luka Strizic'

@login_required
@app.route("/super/admin/approveRequestCallback", methods=["POST"])
def registration_requests():
    data = request.form
    id = data["id"]
    req = Functions.get_request_by_id(id)

    doc = None
    if req['type'] == 'worker':
        doc = user.UserDocument()
        doc['username'] = basestring
        doc['password'] = basestring
        doc['type'] = basestring
        doc['name'] = basestring
        doc['surname'] = basestring
        doc['city'] = basestring
        doc['address'] = basestring
        doc['institutionID'] = basestring
        doc.save()
    elif req['type'] == 'institution':
        doc = institution.InstitutionDocument()
        doc['name'] = req['name']
        doc['city'] = req['city']
        doc['address'] = req['address']
        doc.save()

    return render_template("admin/registrationRequests.html",
                           worker_registation_requests = Functions.pull_registration_requests("worker"),
                           institution_registation_requests = Functions.pull_registration_requests("institution"),
                           total_requests_num = total_requests_num,
                           user=current_user)
