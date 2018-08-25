from flask import Flask, request, jsonify, session, make_response, after_this_request, abort
import json
import sys
import os
from auth import authorize

app = Flask(__name__)

app.config.update(
    SECRET_KEY='Ijb8u#vjklawD9da34hQnad,wo[1]aa[',
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_NAME='authtest'
)



@app.before_request
def init_session():
    pass


@app.route("/api/login", methods=['POST'])
def login_post():
    data = {
        'result': False
    }
    form = request.get_json()
    print(form)
    if form.get('username') and form.get('groups'):
        session['user'] = {
            'username': form.get('username'),
            'groups': form.get('groups')}
        data['result'] = session['user']

    return jsonify(data)

@app.route("/api/logout", methods=['POST'])
def logout_post():
    data = {'result': ''}
    try:
        session.clear()
        data['result'] = 'logged out'
    except Exception as e:
        pass
    return jsonify(data)

@app.route("/api/session", methods=['GET'])
def session_get():
    # abort(401)
    data = {
        'result': False
    }
    if session.get('user'):
        data['result'] = session['user']

    return jsonify(data)


@app.route("/api/check-member", methods=['GET'])
@authorize(['Member'])
def check_member():
    return jsonify({'result': 'Good'})

@app.route("/api/check-login", methods=['GET'])
@authorize()
def check_login():
    return jsonify({'result': 'Good'})

@app.route("/api/check-multiple", methods=['GET'])
@authorize(['Manager', 'Subscriber'])
def check_multiple():
    return jsonify({'result': 'Good'})
