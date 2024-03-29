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
Focus on the following files and folders:
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
├──
├── environment.yml
├── requirements.txt
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
### 1. Download datasets
This project utilizes two datasets: [The Oxford Buildings Dataset](https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/) and [The Paris Dataset](https://www.robots.ox.ac.uk/~vgg/data/parisbuildings/). Due to the [licensing terms](https://www.robots.ox.ac.uk/~vgg/terms/dataset-group-2-access.html) for these datasets, we are unable to share them directly. You need to download yourself.
- Download, unzip, and place all images of each dataset in the appropriate folder as shown in the tree structure above.
- Note that the Paris dataset contains [20 corrupted images](https://www.robots.ox.ac.uk/~vgg/data/parisbuildings/corrupt.txt). After downloading the dataset, it will be necessary to delete these files.

`feature` folder: download [here](https://drive.google.com/file/d/1KEmSnVfyMWs6ydP5mbFf0SZAb2HY0aob/view?usp=share_link)

`uploaded` folder: must be created before running the project.

### 2. Install required libraries
! NOTE: This project using `Python v3.10.9`
#### a) Anaconda
After clone the repository and download all necessary folder, run the command
```sh
conda env create -f environment.yml --name env_name
```
Place the **env_name** with the name you want  

#### b) PIP
If you don't have Anaconda installed, use the command to create a virtual environment.
```
virtualenv myenv --python=python3.10.9
```
Activate the virtual environment by running the following command:
```
source myenv/bin/activate
```
Install the libraries:
```
pip install -r requirements.txt
```

### 3. Start web server
**cd** to parent folder and run the command
```sh
flask --app server.py run
```
or 
```sh
python server.py
```
The system will automatically load the necessary data. When finished,
Ctrl + left click the URL: `http://127.0.0.1:5000`.

## III. Demo
Click this image below
[![Demo](https://github.com/ShenggKai/CBIR_System/blob/master/static/image/demo.png?raw=true)](https://youtu.be/gct-OMgGbPE)
