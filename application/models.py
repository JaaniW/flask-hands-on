import datetime

from . import db

class User(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(150), unique=True, index=True)
    password = db.Column(db.String(250))
    date_of_birth = db.Column(db.DateTime(), default=datetime.datetime.utcnow, index=True)
    # is_admin =  
    # is_staff =  
    # is_superuser =  

