import re
import os
import sys
from datetime import datetime
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt





asba_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ABSA'))


sys.path.insert(0, asba_path)


from flask import Flask, render_template, request
from markupsafe import Markup
from ABSA import run_absa




app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'], endpoint='home')
def articleanalysis():
    if request.method == 'GET':
        return render_template('forms.html')


    article = request.form.get('Title')
    word = request.form.get('Analysis word')


    result = run_absa(word, article)

    # --- Safely extract values using regex ---
    sentiment_dict = dict(re.findall(r'(\w+)\s*=\s*([\d.]+)', result))
    sentiment_dict = {k: float(v) for k, v in sentiment_dict.items()}

    # Plotting as before
    labels = list(sentiment_dict.keys())
    values = list(sentiment_dict.values())

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['red', 'gray', 'green'])
    plt.title('Sentiment Analysis')
    plt.ylabel('Score')

    # Save image
    img_path = os.path.join("static", "sentiment_plot.png")
    plt.savefig(img_path)
    plt.close()

    print(f"Saving image to: {img_path}")

    return render_template('forms.html', result=result, image_url=img_path)

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


@app.route('/bbcdata/')
def bbcdata():
    with open("../dataset/raw_news_titles/bbc_news_titles.csv", 'r', encoding="utf-8") as bbc_file:
        bbc_data = list(csv.reader(bbc_file))
    return render_template('cvsdisplay.html', data=bbc_data)

@app.route('/cbcdata/')
def cbcdata():
    with open("../dataset/raw_news_titles/cbc_news_titles.csv", 'r', encoding="utf-8") as cbc_file:
        cbc_data = list(csv.reader(cbc_file))
    return render_template('cvsdisplay.html', data=cbc_data)

@app.route('/npydata/')
def nypdata():
    with open("../dataset/raw_news_titles/nyp_news_titles.csv", 'r', encoding="utf-8") as nyp_file:
        nyp_data = list(csv.reader(nyp_file))
    return render_template('cvsdisplay.html', data=nyp_data)

if __name__ == "__main__":
    app.run(debug=True)