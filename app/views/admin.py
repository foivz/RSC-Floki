from flask import render_template
from flask.ext.login import current_user, login_required
from app import app
from app.core import Functions

__author__ = 'Davor Obilinovic'

@login_required
@app.route("/super/admin/registrationRequests", methods=["GET"])
def registration_requests():
    worker_registation_requests = Functions.pull_registration_requests("worker")
    institution_registation_requests = Functions.pull_registration_requests("institution")
    total_requests_num = len(worker_registation_requests) + len(institution_registation_requests)
    return render_template("admin/registrationRequests.html",
                           worker_registation_requests = worker_registation_requests,
                           institution_registation_requests = institution_registation_requests,
                           total_requests_num = total_requests_num,
                           user=current_user)

