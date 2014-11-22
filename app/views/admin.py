from flask import render_template
from flask.ext.login import current_user
from app import app
from app.core import Functions

__author__ = 'Davor Obilinovic'


@app.route("/super/admin", methods=["GET"])
def super_admin():
    return render_template("admin/registrationRequests.html",
                           worker_registation_requests = Functions.pull_registration_requests("worker"),
                           institution_registation_requests = Functions.pull_registration_requests("institution"),
                           user=current_user)