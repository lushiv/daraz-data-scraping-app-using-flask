import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))
import requests 
from requests.utils import requote_uri
import json
import ast 
from flask import jsonify
from flask import Flask,request,render_template,redirect

from flask_app.methods import daraz_scraper


app = Flask(__name__)


@app.route('/')
def test_base_api():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,host= '0.0.0.0', port='5001')
