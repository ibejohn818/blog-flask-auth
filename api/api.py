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
    session['user'] = {}
    session['user']['username'] = request.form.get('username', 'default user')
    session['user']['groups'] = [ g.strip() for g in request.form.get('groups').split(',') ]
    return jsonify(session['user'])

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
    print(request.__dict__)
    data = {}
    if session.get('user'):
        data['username'] = session.get('user').get('username')
        data['groups'] = session.get('user').get('groups')
    return jsonify(data)


@app.route("/api/check-member", methods=['GET'])
@authorize(['Member'])
def check_member():
    return jsonify({'result': 'Good'})
