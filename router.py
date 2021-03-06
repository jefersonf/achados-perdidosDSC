#coding: utf-8
# pylint: disable=C0103

"""This module represents the backend portion of our achados_e_perdidos project"""

import os
import uuid
import sqlite3
import json
import sys

from core.controller import Controller

from flask import Flask
from flask import render_template
from flask import request, redirect, g, send_file
from flask import flash
from flask_mail import Mail, Message


reload(sys)
sys.setdefaultencoding("utf-8")

#-------------------- CONFIG --------------------

TEMPLATE_DIR = os.path.abspath('static')
app = Flask(__name__, template_folder=TEMPLATE_DIR)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = './uploads'

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def init_db():
    """Initializes the db"""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

#---------------------- MAIL------------------

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mimacher.dsc@gmail.com'
f = open('pass.txt', 'r') # From wherever they upload it to.
read = f.read()
app.config['MAIL_PASSWORD'] = read
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

#---------------------- DB --------------------

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'

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
    PORT_NUMBER = int(os.environ.get('PORT', 5000))
    app.config.update(DEBUG=True, TEMPLATES_AUTO_RELOAD=True)
    app.run(host='127.0.0.1', port=PORT_NUMBER)

# -------------------------AUX FUNCTIONS------------

def allowed_file(filename):
    """Checks if a filename if between the allowed files"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ----------------------------------STATIC---------------------------------------
controller = Controller()


def send_email(recipient, token):
    """Sends an email to a user with the token"""
    print recipient
    msg = Message('Código de acesso para o achados e perdidos!',\
     sender='mimacher.dsc@gmail.com', recipients=[str(recipient)])
    msg.body = "Olá, obrigado por fazer parte da comunidade do achados e perdidos!\n\
    Aqui está seu código de acesso para o objeto registrado:\n\n" + token
    mail.send(msg)
    return "Sent"


def show_entries(entries):
    """render the template with the given entries"""
    return render_template('index.html', entries=entries)


@app.route('/')
def root():
    """render the template with all entries"""
    db = get_db()
    cur = db.execute('select name, text, status, id from entries order by id desc')
    entries = cur.fetchall()
    return show_entries(entries)


@app.route('/image/<itemId>')
def get_image(itemId):
    """Returns a image according to the itemid"""
    print itemId
    path = "./uploads/" + str(itemId) + ".jpg"
    return send_file(path, mimetype='image/jpg')


def generate_token():
    """Generates a token randomly"""
    db = get_db()
    cur = db.execute('select token, status from tokens')
    entries = cur.fetchall()

    token = str(uuid.uuid4().hex)

    while True:
        is_repeated = False

        for entry in entries:
            if token in entry:
                is_repeated = True

        if not is_repeated:
            break
        else:
            token = str(uuid.uuid4().hex)

    return token


@app.route('/item', methods=['POST'])
def add_item():
    """Add an lost or found item into the db"""
    db = get_db()
    print request.form

    token = generate_token()
    token_insertion_query = 'insert into tokens (token, status) values (?, ?)'
    cur0 = db.execute(token_insertion_query, (token, 'not_used'))
    token_id = cur0.lastrowid

    cur = db.execute('\
    insert into entries (name, text, status, category, user_email ,token_id)\
     values (?, ?, ?, ?, ?, ?)',\
     [request.form['name'], request.form['text'], request.form['inlineRadioOptions'],\
      request.form['category'], request.form['email'], token_id])

    send_email(request.form['email'], token)

    db.commit()
    itemId = cur.lastrowid
    print request.files
    if 'file' not in request.files:
        print "nao achou"
    else:
        filee = request.files['file']
        if filee and allowed_file(filee.filename):
            filename = str(itemId) + "." + filee.filename.rsplit('.', 1)[1].lower()
            print filename
            filee.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect("/")


@app.route('/icone/<itemId>')
def get_icon(itemId):
    print(itemId)
    path = "./uploads/" + str(itemId) + ".png"
    print path

    return send_file(path, mimetype='image/png')


def get_token(token_id):
    """Get token given id"""
    db = get_db()
    cur = db.execute('select token, status from tokens where id =' + '"' + str(token_id) + '"')
    entries = cur.fetchall()

    if len(entries) > 0:
        return entries[0]
    else:
        #FLAG TO INDICATE ERROR
        return -1


@app.route('/item', methods=['GET'])
def get_all():
    """Returns all entries from the db"""
    db = get_db()
    cur = db.execute('select name, text, status, category, user_email, id \
    from entries order by id desc')
    entries = cur.fetchall()
    dic = {}
    dic['item'] = []
    for entry in entries:
        aux = {'title':entry[0], 'description': entry[1], 'status':entry[2],\
         'category':entry[3], 'user_email':entry[4], 'id':entry[5]}
        dic['item'].append(aux)
    return json.dumps(dic)


def validate_token(id, user_token):
    """Check whether a token is valid or not"""
    db = get_db()
    cur = db.execute('select name, text, status, category, token_id, id \
    from entries where id =' + '"' + id + '"')
    entries = cur.fetchall()

    token_id = entries[0][4]
    token = get_token(token_id)
    if token == -1:
        return False

    return token[0] == user_token.strip()


def return_item(item_id):
    """Returns an item given the id"""
    db = get_db()
    db.execute('update entries set status=? where id = ?', ("returned", item_id))
    db.commit()


@app.route('/update-item', methods=['POST'])
def update_item():
    """Updates the information of an item"""
    token = request.form['access-code']
    item_id = request.form['item-id']

    if validate_token(item_id, token):
        return_item(item_id)
        return redirect("/")

    else:
        flash("Codigo de acesso incorreto")
        return redirect("/")


@app.route('/achados', methods=['GET'])
def get_achados():
    """Returns the found items"""
    db = get_db()
    cur = db.execute('select name, text, status, category\
     from entries where status = "option1" order by id desc')
    entries = cur.fetchall()
    dic = {}
    dic['item'] = []
    for entry in entries:
        aux = {'title':entry[0], 'description': entry[1], 'status':entry[2], 'category':entry[3]}
        dic['item'].append(aux)
    return json.dumps(dic)


@app.route('/perdidos', methods=['GET'])
def get_perdidos():
    """Returns the lost items"""
    db = get_db()
    cur = db.execute('select name, text, status, category\
     from entries where status = "option2" order by id desc')
    entries = cur.fetchall()
    dic = {}
    dic['item'] = []
    for entry in entries:
        aux = {'title':entry[0], 'description': entry[1], 'status':entry[2], 'category':entry[3]}
        dic['item'].append(aux)
    return json.dumps(dic)


@app.route('/category/<category>', methods=['GET'])
def get_by_category(category):
    """Returns items from a category"""
    db = get_db()
    cur = db.execute('select name, text, status, category\
     from entries where category =' + '"' + category + '"' + 'order by id desc')
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
