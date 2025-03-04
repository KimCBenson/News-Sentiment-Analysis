import re
import os
from datetime import datetime
import csv

from flask import Flask

from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/cnndata/')
def cnndata():
    data = []
    file_path = os.path.join('..','dataset', 'cnnarticles.csv')
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return render_template('cvsdisplay.html', data=data)

@app.route('/nprdata/')
def nprdata():
    npr_data = []
    npr_path = os.path.join('..','dataset', 'nprarticles.csv')
    with open(npr_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            npr_data.append(row)
    return render_template('cvsdisplay.html', data=npr_data)

@app.route('/nytdata/')
def nytdata():
    nyt_data = []
    nyt_path = os.path.join('..', 'dataset', 'nytarticles.csv')
    with open(nyt_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            nyt_data.append(row)
    return render_template('cvsdisplay.html', data=nyt_data)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "website.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

