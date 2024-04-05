from datetime import datetime
from flask import current_app
from app import db

class Guests(db.Model): 
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), primary_key=False)
    email = db.Column(db.String(255), primary_key=False)
    received = db.Column(db.Boolean, primary_key=False)
    check_in = db.Column(db.Boolean, primary_key=False)
    time = db.Column(db.String(255), primary_key=False)
