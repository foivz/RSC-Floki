import ConfigParser
from mongokit import Connection

__author__ = 'Davor Obilinovic'


configParser = ConfigParser.RawConfigParser()
configParser.read("config.txt")

def get_connection():
    conn = Connection("localhost", 27017)
    dbauth = conn.Magic2.authenticate(configParser.get("Mongo","username"),configParser.get("Mongo","password"))
    return conn

mongo = get_connection()