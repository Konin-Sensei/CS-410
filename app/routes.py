import pygal
from app import application
from flask import render_template, jsonify, redirect, send_file, request
from werkzeug.utils import secure_filename
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import xlrd
import pandas as pd
import numpy as np
import json
from app.graph import create_plot
from app.graph import create_plot2



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
    print("HI")
    return render_template('parameters.html')


@application.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        df = pd.read_excel(request.files.get('file'))
        choro = create_plot2(df)
        choice = create_plot(df)
    return render_template('plotme.html', plot=choro, plot1=choice)

