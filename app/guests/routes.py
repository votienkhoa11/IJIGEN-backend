from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask.json import jsonify
from sqlalchemy import create_engine
from app.models import Guests
from app.config import Config
from app import db, bcrypt
from app.utils.send_email import send_email
import pandas as pd

guests = Blueprint('guests', __name__)


@guests.route('/input-data', methods=['GET'])
def input_data():
    msg = ''
    try:
        data = pd.read_csv('data.csv', index_col=False, delimiter=',')
        engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

        data.to_sql('guests',engine,if_exists='replace')
        msg='successfully added'
    except NameError:
        msg = 'An error occurred!' 
    return jsonify(msg)


@guests.route('/auto-send-email', methods=['GET'])
def auto_send_email():
    msg = ''
    try:
        guests = Guests.query.all()

        for guest in guests:
            send_email(id=guest.id, name=guest.name, email=guest.email)
        msg = 'Sucessfully operated'
    except:
        msg = 'error occured'
    return jsonify(msg)


@guests.route('/send-email', methods=['GET'])
def send_email1():
    msg = ''

    guests = [
        {
            'id': 'IJIGEN-T67',
            'name': 'AoiChi',
            'email': 'roxycf1993@gmail.com',
        },

    ]

    for index in range(len(guests)):
        send_email(id=guests[index]['id'], name=guests[index]['name'], email=guests[index]['email'])
    msg = 'Sucessfully operated'

    return jsonify(msg)


@guests.route('/check-in', methods = ['PUT', 'GET'])
def check_in_guest():
    msg = ''
    res = {}
    try:
        idArg = request.args.get('id')
        guest = Guests.query.filter_by(id=idArg).first()
        guest.check_in = 1
        db.session.commit()
        
        msg = 'success'

        res ={
            'status': msg
        }
        return jsonify(res)
    except:
        msg = 'error'

        res = {
            'status': msg
        }
        return jsonify(res)


@guests.route('/get-user-by-id', methods = ['GET'])
def get_user_by_id():
    msg = ''

    idArg = request.args.get('id')
    try:
        guest = Guests.query.filter_by(id=idArg).first()
        guest = {
            'id': guest.id,
            'name': guest.name,
            'email': guest.email,
            'check_in': guest.check_in,
        }

        msg = 'success'
        res = {
            'status': msg,
            'data': guest,
        }

        return jsonify(res)
    except:
        msg = 'An error occurred!'
        res = {
            'status': msg,
        }
        return jsonify(res)


@guests.route('/get-all-guests', methods=['GET'])
def get_all_guest():
    msg = ''
    try:
        guests = Guests.query.all()
        result_list = []
        for guest in guests:
            guest = {
                'id': guest.id,
                'name': guest.name,
                'email': guest.email,
                'check_in': guest.check_in,
            }
            result_list.append(guest)

        msg = 'success'
        res = {
            'status': msg,
            'data': result_list,
        }
        return jsonify(res)
    except:
        msg = 'error occured'
        res = {
            'status': msg,
        }
        return jsonify(msg)
   

@guests.route('/get-checkin-guests', methods=['GET'])
def get_checkin_guest():
    checkin = request.args.get('checkin')
    msg = ''
    try:
        guests = Guests.query.filter_by(check_in=checkin).all()
        result_list = []
        for guest in guests:
            guest = {
                'id': guest.id,
                'name': guest.name,
                'email': guest.email,
                'check_in': guest.check_in,
            }
            result_list.append(guest)

        msg = 'success'
        res = {
            'status': msg,
            'data': result_list,
        }
        return jsonify(res)
    except:
        msg = 'error'
        res = {
            'status': msg,
        }
        return jsonify(res)