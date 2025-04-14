import re
import os
import sys
from datetime import datetime
import csv


asba_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ASBA prototype'))

sys.path.insert(0, asba_path)

from flask import Flask, render_template, request
from markupsafe import Markup
from BasicABSA import run_absa


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
    with open("../dataset/raw_news_titles/cnnarticles.csv", 'r', encoding='utf-8') as file:
        data = list(csv.reader(file))
    return render_template('cvsdisplay.html', data=data)

@app.route('/nprdata/')
def nprdata():
    with open("../dataset/raw_news_titles/nprarticles.csv", 'r', encoding="utf-8") as npr_file:
       npr_data = list(csv.reader(npr_file))
    return render_template('cvsdisplay.html', data=npr_data)

@app.route('/nytdata/')
def nytdata():
    with open("../dataset/raw_news_titles/nytarticles.csv", 'r', encoding="utf-8") as test_file:
       test_data = list(csv.reader(test_file))
    return render_template('cvsdisplay.html', data=test_data)

@app.route('/foxdata/')
def foxdata():
    with open("../dataset/raw_news_titles/fox_news_titles.csv", 'r', encoding="utf-8") as fox_file:
        fox_data = list(csv.reader(fox_file))
    return render_template('cvsdisplay.html', data=fox_data)

@app.route('/articleanalysis/', methods=['GET', 'POST'])
def articleanalysis():
    if request.method == 'GET':
        return render_template('forms.html')

    article = request.form.get('Title')
    word = request.form.get('Analysis word')

    result = run_absa(word, article)
    return render_template('forms.html', result=result)

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

if __name__ == "__main__":
    app.run(debug=True)