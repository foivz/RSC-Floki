from flask import render_template
from flask.ext.login import current_user, login_required
from app import app
from app.core import Functions
import app.DAO.institution as institution

__author__ = 'Davor Obilinovic'

@login_required
@app.route("/super/admin/registrationRequests", methods=["GET"])
def registration_requests():
    worker_registation_requests = Functions.pull_registration_requests("worker")
    institution_registation_requests = Functions.pull_registration_requests("institution")
    total_requests_num = len(worker_registation_requests) + len(institution_registation_requests)
    return render_template("admin/registrationRequests.html",
                           worker_registation_requests = Functions.pull_registration_requests("worker"),
                           institution_registation_requests = Functions.pull_registration_requests("institution"),
                           total_requests_num = total_requests_num,
                           user=current_user)

@login_required
@app.route("/super/admin/editInstitutions", methods=["GET"])
def edit_institutions():
    return render_template("admin/editInstitutions.html",
                           institutions=institution.get_all_institutions_array(),
                           user=current_user)