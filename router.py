import os
import datetime

from core.controller import Controller
from core import database

from flask import Flask
from flask import render_template
from flask import Flask, request, redirect, jsonify, abort
from datetime import datetime,  date, timedelta

#-------------------- CONFIG --------------------

app = Flask(__name__)

app.config.update(
	MAX_CONTENT_LENGTH = 1024 * 1024,
	DEBUG = True
	#,SQLALCHEMY_DATABASE_URI = 'sqlite:///app-name.db',
	#SQLALCHEMY_TRACK_MODIFICATIONS = False,
	#SQLALCHEMY_POOL_RECYCLE = 280
)

#---------------------- MAIN --------------------

if __name__ == '__main__':
    port_nr = int(os.environ.get('PORT', 5000))
    app.config.update(DEBUG=True,TEMPLATES_AUTO_RELOAD=True)
    app.run(host='127.0.0.1', port=port_nr)

#----------------------------------STATIC---------------------------------------
controller = Controller()

@app.route('/')
def root():
    return redirect('/site/')

@app.route('/site/')
@app.route('/site/<path:url>')
def render_view(url=None):
    return serve_static('index.html')

@app.route('/<path:url>')
def serve_static(url):
	return app.send_static_file(url)
