import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))
import requests 
from requests.utils import requote_uri
import json
import ast 
from flask import jsonify
from flask import Flask,jsonify, request, render_template,redirect,url_for,flash,send_file
from flask_app.methods import daraz_scraper


from flask_app.methods import daraz_scraper


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/download", methods=["POST", "GET"])
def download():
    if request.method == "POST":

        payload = {
        'scraping_url' : request.form["url"],
        'filename' : request.form["filename"]
        }
        print(payload)
        return_data = daraz_scraper.get_daraz_data(payload)

        return redirect(url_for('download'))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,host= '0.0.0.0', port='5002')
