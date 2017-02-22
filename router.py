import os
import datetime

from core.controller import Controller
from core import database

import sqlite3

from flask import Flask
from flask import render_template
from flask import Flask, request, redirect, jsonify, abort, g
from datetime import datetime,  date, timedelta
import json

#-------------------- CONFIG --------------------

template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

#---------------------- DB --------------------

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

#---------------------- MAIN --------------------

if __name__ == '__main__':
    port_nr = int(os.environ.get('PORT', 5000))
    app.config.update(DEBUG=True,TEMPLATES_AUTO_RELOAD=True)
    app.run(host='127.0.0.1', port=port_nr)

#----------------------------------STATIC---------------------------------------
controller = Controller()

def show_entries(entries):
    return render_template('index.html', entries=entries)

@app.route('/')
def root():
    db = get_db()
    cur = db.execute('select name, text, status from entries order by id desc')
    entries = cur.fetchall()
    return show_entries(entries)

@app.route('/item', methods=['POST'])
def add_item():
    db = get_db()
    db.execute('insert into entries (name, text, status, category) values (?, ?, ?, ?)', [request.form['name'], request.form['text'], request.form['inlineRadioOptions'], "nocategory"])
    db.commit()
    return root()

@app.route('/item', methods=['GET'])
def get_all():
    db = get_db()
    cur = db.execute('select name, text, status, category from entries order by id desc')
    entries = cur.fetchall()
    dic = {}
    dic['item'] = []
    for entry in entries:
        aux = {'title':entry[0], 'description': entry[1], 'status':entry[2], 'category':entry[3]}
        dic['item'].append(aux)
    return json.dumps(dic)

@app.route('/achados', methods=['GET'])
def get_achados():
    db = get_db()
    cur = db.execute('select name, text, status, category from entries where status = "option1" order by id desc')
    entries = cur.fetchall()
    dic = {}
    dic['item'] = []
    for entry in entries:
        aux = {'title':entry[0], 'description': entry[1], 'status':entry[2], 'category':entry[3]}
        dic['item'].append(aux)
    return json.dumps(dic)

@app.route('/perdidos', methods=['GET'])
def get_perdidos():
    db = get_db()
    cur = db.execute('select name, text, status, category from entries where status = "option2" order by id desc')
    entries = cur.fetchall()
    dic = {}
    dic['item'] = []
    for entry in entries:
        aux = {'title':entry[0], 'description': entry[1], 'status':entry[2], 'category':entry[3]}
        dic['item'].append(aux)
    return json.dumps(dic)

@app.route('/category/<category>', methods=['GET'])
def get_by_category(category):
    db = get_db()
    cur = db.execute('select name, text, status, category from entries where category =' + '"' + category + '"' + 'order by id desc')
    entries = cur.fetchall()
    dic = {}
    dic['item'] = []
    for entry in entries:
        aux = {'title':entry[0], 'description': entry[1], 'status':entry[2], 'category':entry[3]}
        dic['item'].append(aux)
    return json.dumps(dic)

@app.route('/site/')
@app.route('/site/<path:url>')
def render_view(url=None):
    return serve_static('index.html')

@app.route('/<path:url>')
def serve_static(url):
	return app.send_static_file(url)
