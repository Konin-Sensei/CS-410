from app import application
from flask import render_template

@application.route('/')

@application.route('/index')
def index():
    return render_template('index.html')

@application.route('/results')
def results():
    return render_template('results.html')

@application.route('/data')
def data():
    return render_template('data.html')

@application.route('/parameters')
def parameters():
    return render_template('parameters.html')
