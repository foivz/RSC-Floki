import ConfigParser
from mongokit import Connection

__author__ = 'Davor Obilinovic'


configParser = ConfigParser.RawConfigParser()
configParser.read("config.txt")

def get_connection():
    conn = Connection(configParser.get("Mongo","host"), int(configParser.get("Mongo","port")))
    dbauth = conn[configParser.get("Mongo","DBname")].authenticate(configParser.get("Mongo","username"),configParser.get("Mongo","password"))
    return conn

mongo = get_connection()