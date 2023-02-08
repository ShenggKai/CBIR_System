import os
import numpy as np
from PIL import Image
from pathlib import Path
# from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")