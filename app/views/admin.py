from flask import render_template
from flask.ext.login import current_user, login_required
from app import app
from app.core import Functions
import app.DAO.institution as institution
import app.DAO.user as user

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

@login_required
@app.route("/super/admin/editInstitutions/<id>", methods=["GET"])
def edit_institution(id):
    return render_template("admin/editInstitution.html",
                           institution=institution.get_by_id(id),
                           user=current_user,
                           id = id)

@login_required
@app.route("/super/admin/editWorkers", methods=["GET"])
def edit_workers():
    return render_template("admin/editWorkers.html",
                           workers=user.get_all_workers_array(),
                           user=current_user)

@login_required
@app.route("/super/admin/editWorkers/<username>", methods=["GET"])
def edit_worker(username):
    return render_template("admin/editWorker.html",
                           worker=user.get_by_username(username),
                           institutions=institution.get_all_institutions_array(),
                           user=current_user)

@login_required
@app.route("/super/admin/editDonors", methods=["GET"])
def edit_donors():
    return render_template("admin/editDonors.html",
                           donors=user.get_all_donors_array(),
                           user=current_user)

@login_required
@app.route("/super/admin/editDonors/<username>", methods=["GET"])
def edit_donor(username):
    return render_template("admin/editDonor.html",
                           donor=user.get_by_username(username),
                           user=current_user)

@login_required
@app.route("/super/admin/sendNotification", methods=["GET"])
def send_notification():
    return render_template("admin/sendNotification.html",
                           user=current_user)