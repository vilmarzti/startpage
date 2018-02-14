from flask import Flask
from bs4 import BeautifulSoup

import urllib
import requests

btcURL = "https://bitcoinity.org"

app = Flask(__name__)


@app.route("/")
def hello():
    with open("index.html", "rw") as outfile:
        a = fillData(outfile)
    return ""


def fillData(html):
    btchtml = getHTML(btcURL)
    html = parseBtcHtml(btchtml, html)


    return html


def getHTML(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    return ""


def parseBtcHtml(btchtml, html):
    soup = BeautifulSoup(btchtml)
    value = soup.find_all("class=value")
    print(value)



def parseWeatherHtml():
    pass


def parseTime():
    pass
