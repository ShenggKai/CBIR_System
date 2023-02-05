![last commit](https://img.shields.io/github/last-commit/ShenggKai/CBIR_System?logo=git)
![repo size](https://img.shields.io/github/repo-size/ShenggKai/CBIR_System?logo=github)
![code size](https://img.shields.io/github/languages/code-size/ShenggKai/CBIR_System?logo=GitHub)
![license](https://img.shields.io/github/license/ShenggKai/CBIR_System)
![Made with love in Vietnam](https://madewithlove.now.sh/vn?heart=true&colorB=%23da251d)
# CS336: Multimedia Information Retrieval 2023
Final Project: Project 2 - Image Retrieval  
Supported features:
- Retrieval methods DELF, CNN (ResNet), CNNIRPYTORCH are available on web app.
- Particular object search: allow user to choose a specific area of the query image.

## I. Contributors
|Name|Email|Github profile|
|:-:|:-:|:-:|
|Nguyễn Quốc Đạt|19521338@gm.uit.edu.vn|[ShenggKai](https://github.com/ShenggKai)|
|Hồ Bảo Quốc Thắng|19520271@gm.uit.edu.vn|[-](https)|
|Trương Quốc Bình|19521270@gm.uit.edu.vn|-|

## II. Repo structure
Overview
```
.
├── ...
├── retrieval.py
├── app.py
├── static
│   ├── features
│   ├── images
│   ├── query
│   └── uploads
└── templates
```

other:
```
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

Files:
- **./app.py**: flask web server.
- **./retrieval.py**: retrieve images (standalone).

Folders:
- **./static/**: contains 2 datasets including features and 256x256 resized version, uploaded query images.

## III. Usage
You can clone this repo and install datasets separately or you can download the whole compressed file that we have already downloaded and structured.

### 1. Install datasets separately

Datasets use for the project:  
- [**Oxford Buildings Dataset**](https://www.robots.ox.ac.uk/~vgg/data/oxbuildings/) (5062 images)
- [**Paris Dataset**](https://www.robots.ox.ac.uk/~vgg/data/parisbuildings/) (6412 images - 20 images are corrupted, list of corrupt images is available [here](https://www.robots.ox.ac.uk/~vgg/data/parisbuildings/corrupt.txt))

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
