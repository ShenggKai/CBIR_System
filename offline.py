from PIL import Image
from feature_extractor import FeatureExtractor
from tqdm import tqdm
import numpy as np
import os

data_folder = r"static\image"
feature_folder = r"static\feature"

fe = FeatureExtractor()

if __name__ == "__main__":
    for image_path in tqdm(os.listdir(data_folder)):
        image_path_full = os.path.join(data_folder, image_path)

        feature = fe.extract(image=Image.open(image_path_full))
        # exclude .jpg extension by splitext
        feature_path = os.path.join(feature_folder,os.path.splitext(image_path)[0] + ".npy")

        np.save(feature_path, feature)