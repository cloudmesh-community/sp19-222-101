import requests
import numpy as np
from sklearn.externals.joblib import Memory
from sklearn.datasets import load_svmlight_file
from sklearn.svm import SVC
from os import listdir
from flask import Flask, request

#url = 'https://drive.google.com/uc?export=download&id=12u9eviakwqiqsz7x8Sp1ybG9uBaF9bJV'
url = 'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass/glass.scale'

def download_data(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)

def download(output):
    output_file = 'data/'+output
    download_data(url=url, filename=output_file)
    return "Data Downloaded"
