import pygal
from app import application
from flask import render_template, jsonify, redirect, send_file, request
from werkzeug.utils import secure_filename
import pandas as pd
import matplotlib.pyplot as plt

books = [
    {
        'name': 'Grener',
        'price': 10.00
    },
    {
        'name': 'Cow',
        'price': 11.00
    }
]


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
        df = pd.read_csv(request.files.get('file'))
        graph1 = plt.plot(range(100))
    return render_template("graphing10.html")


@application.route('/pygalexample')
def pygalexample():
    try:
        graph = pygal.Line()
        graph.title = '% Change Coolness of programming languages over time.'
        graph.x_labels = ['2011', '2012', '2013', '2014', '2015', '2016']
        graph.add('Python', [15, 31, 89, 200, 356, 900])
        graph.add('Java', [15, 45, 76, 80, 91, 95])
        graph.add('C++', [5, 51, 54, 102, 150, 201])
        graph.add('All others combined!', [5, 15, 21, 55, 92, 105])
        graph_data = graph.render_data_uri()
        return render_template("graphing.html", graph_data=graph_data)
    except Exception as e:
        return str(e)
