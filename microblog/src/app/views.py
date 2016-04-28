__author__ = 'user'
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'My Friend'}
    posts = [{'author': {'nickname': 'John'},
             'body': 'Test Post body here'},
             {'author': {'nickname': 'Hopkins'},
              'body': 'Niganiganiggga!!'},
             {'author': {'nickname': 'Whois'},
              'body': 'Knigaknigakniga!!'}]
    return render_template("index.html", title='Home', user=user, posts=posts)
