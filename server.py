import os
import numpy as np
from PIL import Image
from pathlib import Path
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template


app = Flask(__name__)


# User choose between looking for in Oxford data or Paris data, default is Oxford
selected_data_folder = "static/dataset/Oxford5k"

#read image features
fe = FeatureExtractor()
features = []
image_paths = []

if selected_data_folder == "static/dataset/Paris6k": # if Paris
    selected_feature_folder = "static/feature/paris_feature"

    for feature_path in os.listdir(selected_feature_folder):
        '''
        feature_path : "paris_defense_000000.npy"
        +
        selected_feature_folder : "static/feature/paris_feature"
        =
        feature_path_full : "static/feature/paris_feature/paris_defense_000000.npy"
        ______________________________________________________________
        selected_data_folder : "static/dataset/Paris6k"
        +
        feature_path - ".npy" + ".jpg": "paris_defense_000000.jpg"
        =
        image_paths : "static/dataset/Paris6k/paris_defense_000000.jpg"
        '''

        feature_path_full = os.path.join(selected_feature_folder, feature_path)
        features.append(np.load(feature_path_full))
        image_paths.append(os.path.join(selected_data_folder, os.path.splitext(feature_path)[0] + ".jpg"))

else: # if Oxford
    selected_feature_folder = "static/feature/oxford_feature"

    for feature_path in os.listdir(selected_feature_folder):
        '''
        feature_path : "all_souls_000000.npy"
        +
        selected_feature_folder : "static/feature/oxford_feature"
        =
        feature_path_full : "static/feature/oxford_feature/all_souls_000000.npy"
        ______________________________________________________________
        selected_data_folder : "static/dataset/Oxford5k"
        +
        feature_path - ".npy" + ".jpg": "all_souls_000000.jpg"
        =
        image_paths : "static/dataset/Oxford5k/all_souls_000000.jpg"
        '''

        feature_path_full = os.path.join(selected_feature_folder, feature_path)
        features.append(np.load(feature_path_full))
        image_paths.append(os.path.join(selected_data_folder, os.path.splitext(feature_path)[0] + ".jpg"))

# convert features to numpy array
features = np.array(features)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET","POST"])
def results():
    # file = request.files["query_img"]

    # #save query image
    # img = Image.open(file.stream)
    # uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
    # img.save(uploaded_img_path)

    # #run search
    # query = fe.extract(img)
    # dists = np.linalg.norm(features - query, axis=1) #compute L2 distance between query and all images
    # ids = np.argsort(dists)[:30] # top 30 results
    # scores = [(dists[id], image_paths[id]) for id in ids]

    # return render_template("result.html", query_path=uploaded_img_path, scores=scores)
    return "dumemay"



if __name__ == "__main__":
    app.run(debug=False)