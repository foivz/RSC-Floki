from flask import render_template
from flask.ext.login import login_required, current_user
from app import app

__author__ = 'Davor Obilinovic'

@app.route('/')
@login_required
def index():
    return render_template('index.html',
                           user=current_user)
