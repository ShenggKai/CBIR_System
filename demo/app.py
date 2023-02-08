import os
import numpy as np
from PIL import Image
from pathlib import Path
# from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():
    image_url = request.form['image-url']
    response = requests.get(image_url)
    if response.status_code == 200:
        with open("image.jpg", "wb") as f:
            f.write(response.content)
            
        image_path = request.args.get('image_path')
        return render_template("result.html", image_path=image_path)
    else:
        return 'Error: Could not retrieve image'
