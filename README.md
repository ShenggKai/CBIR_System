![last commit](https://img.shields.io/github/last-commit/ShenggKai/CBIR_System?logo=git)
![license](https://img.shields.io/github/license/ShenggKai/CBIR_System)
![Made with love in Vietnam](https://madewithlove.now.sh/vn?heart=true&colorB=%23da251d)
# Content-Based Image Retrieval System

## I. Overview
    CS336: Multimedia Information Retrieval 2023
    Final Project: Project 2 - Image Retrieval

### Intro
This is a web-based project that implements a content-based image retrieval system (search for images that are similar in content to a query image).  

The system allow users to select a region of an image instead of the entire image as the query.

### Project layout
To get started, focus on the following files and folders:
```
.
├── ...
├── evaluation/
├── static/
│   ├── *dataset/
│   │   ├── Oxford5k
│   │   │   ├── all_souls_000000.jpg
│   │   │   └── ...
│   │   └── Paris6k
│   │   │   ├── paris_defense_000000.jpg
│   │   │   └── ...
│   ├── *feature/
│   ├── *uploaded/
│   └── ...
├── templates/
│   ├── index.html
│   ├── result.html
│   └── ...
├── feature_extractor.py
├── offline.py
├── server.py
├── LICENSE
└── README.md
```
- Place an `*` before the `dataset`, `feature`, `uploaded` folder, as these items and their sub-folders are not included in the repository. See [Download datasets](#1-download-datasets)
- `offline.py`: This script extracts a deep-feature from each database image. Each feature is a 4096D fc6 activation from a VGG16 model with ImageNet pre-trained weights.  
- `server.py`: This script runs a web-server. You can send your query image to the server via a Flask web-interface. The server finds similar images to the query by a simple linear scan.

## II. Usage
You can clone this repo and install datasets separately or you can download the whole compressed file that we have already downloaded and structured.

### 1. Download datasets
This project utilizes two datasets: [The Oxford Buildings Dataset](https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/) and [The Paris Dataset](https://www.robots.ox.ac.uk/~vgg/data/parisbuildings/). Due to the [licensing terms](https://www.robots.ox.ac.uk/~vgg/terms/dataset-group-2-access.html) for these datasets, we are unable to share them directly. You need to download yourself.
- Download, unzip, and place all images of each dataset in the appropriate folder as shown in the tree structure above.
- Note that the Paris dataset contains [20 corrupted images](https://www.robots.ox.ac.uk/~vgg/data/parisbuildings/corrupt.txt). After downloading the dataset, it will be necessary to delete these files.

`feature` and `uploaded` folder: must be created before running the project.


Download the compressed file [here](https://) and we require user an extra structuring step, **./static** should look like this:

```
static
├── features
│   ├── feature
│   ├── feature_oxford
│   ├── feature_oxford_2
│   └── feature_paris
└── images
    ├── database_oxford
    ├── database_paris
    ├── resized_oxford
    └── resized_paris

```

### 2. Install the whole structured folder 
This compressed file requires no further resource downloads or structuring.  
[Download](https://)
### 3. Install required libraries
**./requirements.txt**  
and
```sh
pip install torch===1.5.0 torchvision===0.6.0 -f https://download.pytorch.org/whl/torch_stable.html
```
### 4. Start web server
**cd** to top level folder
```sh
flask run
```
or 
```sh
python app.py
```

If correctly configured, server will be accessible at http://127.0.0.1:5000.

### 5. Query image without starting web server
As we have mentioned above, we will use **./retrieval.py**. We're too lazy too add some extra lines of code to implement command line call, so you have to directly run the file itself.  

Example:
```py
retrieval_image("<query_img_full_path>", "<method>", "<dataset>")
```

## IV. Demo
Yes, we do support image cropping, directly click into the image to crop it!  
Of course the cropped part will be the new query.
![Demo](https://i.imgur.com/5qKLLww.png)

**Video:**
![Demo](https://i.imgur.com/LzP7kf4.png)

## V. Authors
|Name|Email|Student ID|
|:-:|:-:|:-:|
|Nguyễn Quốc Đạt|19521338@gm.uit.edu.vn|19521338
|Hồ Bảo Quốc Thắng|19520271@gm.uit.edu.vn|19520271
|Trương Quốc Bình|19521270@gm.uit.edu.vn|19521270