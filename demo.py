# import os
# import numpy as np
# from PIL import Image
# from pathlib import Path
# from feature_extractor import FeatureExtractor

# fe = FeatureExtractor()
# features = []
# image_paths = []

# selected_data_folder = "static/dataset/Oxford5k"
# selected_feature_folder = "static/feature/oxford_feature"

# for feature_path in os.listdir(selected_feature_folder)[:20]:
#     feature_path_full = os.path.join(selected_feature_folder, feature_path)

#     features.append(np.load(feature_path_full))
#     image_paths.append(os.path.join(selected_data_folder, os.path.splitext(feature_path)[0] + ".jpg"))

# features = np.array(features)

# img = Image.open("static/image/review.jpg")
# #search
# query = fe.extract(img)
# dists = np.linalg.norm(features - query, axis=1) #compute L2 distance between query and all images
# ids = np.argsort(dists)[:30] # top 30 results
# # scores have format: score, image_path, image_name
# scores = [(dists[id], image_paths[id], os.path.basename(image_paths[id])) for id in ids]

# print(scores)

import time

start_time = time.perf_counter()
for i in range(10000000):
    # print(i)
    continue
    # time.sleep(1)
end_time = time.perf_counter()
elapsed = end_time - start_time

print(elapsed)
print(round(elapsed, 2))
