import os
import numpy as np
from tqdm import tqdm
from PIL import Image
from pathlib import Path
from feature_extractor import FeatureExtractor
from datetime import datetime
import time
from flask import Flask, request, render_template


app = Flask(__name__)

#read image features
fe = FeatureExtractor()
default_img_path = "static/image/review.jpg"

paris_features = []
paris_image_paths = []

paris_data_folder = "static/dataset/Paris6k"
paris_feature_folder = "static/feature/paris_feature"

print("____________________________________________")
print("Loading Paris data...")
for feature_path in tqdm(os.listdir(paris_feature_folder)):
    '''
    paris_feature_folder : "static/feature/paris_feature"
    +
    feature_path : "paris_defense_000000.npy"
    =
    feature_path_full : "static/feature/paris_feature/paris_defense_000000.npy"
    ______________________________________________________________
    paris_data_folder : "static/dataset/Paris6k"
    +
    feature_path - ".npy" + ".jpg": "paris_defense_000000.jpg"
    =
    paris_image_paths : "static/dataset/Paris6k/paris_defense_000000.jpg"
    '''

    feature_path_full = os.path.join(paris_feature_folder, feature_path)
    paris_features.append(np.load(feature_path_full))
    paris_image_paths.append(os.path.join(paris_data_folder, os.path.splitext(feature_path)[0] + ".jpg"))
print("Done!")

oxford_features = []
oxford_image_paths = []

oxford__data_folder = "static/dataset/Oxford5k"
oxford_feature_folder = "static/feature/oxford_feature"

print("\nLoading Oxford data ...")
for feature_path in tqdm(os.listdir(oxford_feature_folder)):
    '''
    oxford_feature_folder : "static/feature/oxford_feature"
    +
    feature_path : "all_souls_000000.npy"
    =
    feature_path_full : "static/feature/oxford_feature/all_souls_000000.npy"
    ______________________________________________________________
    oxford__data_folder : "static/dataset/Oxford5k"
    +
    feature_path - ".npy" + ".jpg": "all_souls_000000.jpg"
    =
    oxford_image_paths : "static/dataset/Oxford5k/all_souls_000000.jpg"
    '''

    feature_path_full = os.path.join(oxford_feature_folder, feature_path)

    oxford_features.append(np.load(feature_path_full))
    oxford_image_paths.append(os.path.join(oxford__data_folder, os.path.splitext(feature_path)[0] + ".jpg"))
print("Done!")

# convert features to numpy array
oxford_features = np.array(oxford_features)
paris_features = np.array(paris_features)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/result", methods=["POST"])
def result():
    start = time.perf_counter()

    #take input from user - index.html
    file = request.files["query_img"]
    selected_option = request.form.get("dropdown_dataset")

    image_paths = []
    features = []
    chose_oxford = False # chose Paris

    if selected_option == "oxford": #if oxford is selected
        image_paths = oxford_image_paths
        features = oxford_features
        print("chose Oxford dataset")
        chose_oxford = True
    else: # if paris is selected
        image_paths = paris_image_paths
        features = paris_features
        print("chose Paris dataset")

    
    query_image = "" # for save query image name

    try:
        #save query image
        img = Image.open(file.stream)
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)

        # remove extension .jpg
        query_image = os.path.splitext(file.filename)[0]

    except Exception as e: # if got error, use default image instead
        print("Error reading image:", e)
        print("Use default image")
        img = Image.open(default_img_path)
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + "default.jpg"
        img.save(uploaded_img_path)

        query_image = os.path.basename(default_img_path)
        query_image = os.path.splitext(query_image)[0]

    #run search
    query = fe.extract(img)
    dists = np.linalg.norm(features - query, axis=1) #compute L2 distance between query and all images
    ids = []
    num_results = 0

    if chose_oxford == True:
        ids = np.argsort(dists)[:78] # top 78 results for Oxford dataset
        num_results = 78
    else:
        ids = np.argsort(dists)[:117] # top 117 results for Paris dataset
        num_results = 117


    scores = []
    rank_list = []

    # scores have format: score, image_path, image_name
    for id in ids:
        distance = dists[id]
        image_path = image_paths[id]

        image_name = os.path.basename(image_path)
        rank_list.append(os.path.splitext(image_name)[0])

        score = (distance, image_path, image_name)
        scores.append(score)

    end = time.perf_counter()
    time_elapsed = round(end - start, 2) # round 2 decimal places


    if chose_oxford == True:
        file_path = "evaluation/RlOxford_" + query_image + ".txt"
        print("chose oxford")
    else:
        file_path = "evaluation/RlParis_" + query_image + ".txt"

    # write the rank list to a file
    if not os.path.exists(file_path):
        open(file_path, 'w').close()  # create empty file if it doesn't exist
    with open(file_path, "w") as f:
        f.write("\n".join(rank_list))

    return render_template("result.html", query_path=uploaded_img_path, scores=scores, time_elapsed=time_elapsed, num_results=num_results)



if __name__ == "__main__":
    app.run(debug=False)