from datetime import *
import time
import sys

# First we set our credentials

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return '<h1>This is a Flask App</h1><p>Hello World!</p><p>Linked to jenkins hopefully through github</p><p>Its Alive</p>'

@app.route('/Sub')
def sub_page():
    return '<h2>Sub Page</h2>'    

@app.route('/register', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


