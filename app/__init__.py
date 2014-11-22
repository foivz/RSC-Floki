from flask import Flask
from flask.ext.login import LoginManager
from app.DAO import user

__author__ = 'Davor Obilinovic'


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"
login_manager.session_protection = "strong"


from views import login, pages, admin, callbacks, checks

@login_manager.user_loader
def load_user(userId):
    u = user.get_by_username(userId)
    return u
