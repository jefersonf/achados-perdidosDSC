import os
import datetime

from core.controller import Controller
from core import database

from flask import Flask

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
