import os
import numpy as np
from tqdm import tqdm
from PIL import Image
from pathlib import Path
from feature_extractor import FeatureExtractor
from datetime import datetime


#read image features
fe = FeatureExtractor()
# default_img_path = "static/image/review.jpg"
default_img_path = "static/dataset/Oxford5k/all_souls_000013.jpg"
paris_features = []
paris_image_paths = []

paris_data_folder = "static/dataset/Paris6k"
paris_feature_folder = "static/feature/paris_feature"

print("____________________________________________")
print("Loading Paris data...")
for feature_path in tqdm(os.listdir(paris_feature_folder)[:50]):
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
for feature_path in tqdm(os.listdir(oxford_feature_folder)[:50]):
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

# demo
selected_option = "oxford"

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


# use default image instead
img = Image.open(default_img_path)

#run search
query = fe.extract(img)
dists = np.linalg.norm(features - query, axis=1) #compute L2 distance between query and all images
ids = np.argsort(dists)[:30] # top 30 results
# scores have format: score, image_path, image_name
# scores = [(dists[id], image_paths[id], os.path.basename(image_paths[id])) for id in ids]

scores = []
rank_list = []

for id in ids:
    distance = dists[id]
    image_path = image_paths[id]

    image_name = os.path.basename(image_path)
    rank_list.append(os.path.splitext(image_name)[0])

    score = (distance, image_path, image_name)
    scores.append(score)

# remove path
query_image = os.path.basename(default_img_path)
# remove extension .jpg
query_image = os.path.splitext(query_image)[0]

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

print(scores)