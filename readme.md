# faceRecognition

Course project, facial recognition using  support vector machine (SVM) and principle component analysis (PCA).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project is written in python and used scipy.

```
python		3.6
scipy		1.2.1
```

### Installing

Clone this repository.

```
git clone git@github.com:GlenGGG/FaceRecognition.git
cd FaceRecognition
```

Decompress data.zip

```
unzip data.zip
```

### Usage

Simply run the code.

```
python faceRecognition.py
```

Then you should be able to see some helpful information about the dataset and the result of PCA. In the end, a confusion matrix will be displayed, as well as information about precision, f1-score, recall and support.