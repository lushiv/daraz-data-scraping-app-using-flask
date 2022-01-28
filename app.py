import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))
from flask import Flask, request, render_template
import scraper


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
        return_data = scraper.get_daraz_data(payload)
        return return_data
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,host= '0.0.0.0', port='5002')
