import numpy as np
import os
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path

app = Flask(__name__)

data_folder = r"static\image"
feature_folder = r"static\feature"

#read image features
fe = FeatureExtractor()
features = []
image_paths = []

for feature_path in os.listdir(feature_folder):
    feature_path_full = os.path.join(feature_folder, feature_path)
    features.append(np.load(feature_path_full))
    image_paths.append(os.path.join(data_folder, os.path.splitext(feature_path)[0] + ".jpg"))

features = np.array(features)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["query_img"]

        #save query image
        img = Image.open(file.stream)
        uploaded_img_path = "static\\uploaded\\" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)

        #run search
        query = fe.extract(img)
        dists = np.linalg.norm(features - query, axis=1) #compute L2 distance between query and all images
        ids = np.argsort(dists)[:30] # top 30 results
        scores = [(dists[id], image_paths[id]) for id in ids]

        return render_template("index.html", query_path=uploaded_img_path, scores=scores)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)