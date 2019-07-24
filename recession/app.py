from splinter import Browser
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from flask import Flask, jsonify, render_template, request, redirect
import json
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    executable_path = {'executable_path': os.environ.get('GOOGLE_CHROME_EXE', '') or 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    url = 'https://www.leggmason.com/global/campaigns/clearbridge-aor-recession-indicator-tool.html'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    value = soup.find("span", id="gauge-value").get_text
    
    browser.quit()
    
    return render_template("index.html",percent=int(value)/100, percent2=int(value))

if __name__ == "__main__":
    app.run()

