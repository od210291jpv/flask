__author__ = 'user'
from flask import render_template, flash, redirect
from app import app
from forms import LoginForm
from flask.ext.wtf import Form

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


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title = 'Sign in',
                           form = form)
