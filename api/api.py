from flask import Flask, request, jsonify, session, make_response, after_this_request
import json
import sys
import os
import uuid
import datetime

app = Flask(__name__)

app.config.update(
    SECRET_KEY='Ijb8u#vjklawD9da34hQnad,wo[1]aa[',
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_NAME='authtest'
)



@app.before_request
def init_session():
    pass


@app.route("/", strict_slashes=False)
def index():
    return jsonify({'test': 'admin'})

