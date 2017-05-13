#!/usr/bin/env python
import os
import json
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__, template_folder='../templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {0}!</h1>'.format(name)

###############################################################################

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port=port)
