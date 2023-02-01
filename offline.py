import os
import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from tqdm import tqdm

data_folder_oxford = r"static\dataset\Oxford5k"
data_folder_paris = r"static\dataset\Paris6k"

feature_folder_oxford = r"static\feature\oxford_feature"
feature_folder_paris = r"static\feature\paris_feature"

fe = FeatureExtractor()

if __name__ == "__main__":
    # Extract Oxford features
    print("Extracting Oxford features...")
    for image_path in tqdm(os.listdir(data_folder_oxford)):
        image_path_full = os.path.join(data_folder_oxford, image_path)

        feature = fe.extract(image=Image.open(image_path_full))
        # exclude .jpg extension by splitext
        feature_path = os.path.join(feature_folder_oxford, os.path.splitext(image_path)[0] + ".npy")

        np.save(feature_path, feature)
    
    print("Complete Oxford features extraction!")

    #Extract Paris features
    print("Extracting Paris features...")
    for image_path in tqdm(os.listdir(data_folder_paris)):
        image_path_full = os.path.join(data_folder_paris, image_path)

        feature = fe.extract(image=Image.open(image_path_full))
        # exclude .jpg extension by splitext
        feature_path = os.path.join(feature_folder_paris,os.path.splitext(image_path)[0] + ".npy")
        
        np.save(feature_path, feature)

    print("Complete Paris features extraction!")