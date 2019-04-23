import requests
import numpy as np
from sklearn.externals.joblib import Memory
from sklearn.datasets import load_svmlight_file
from sklearn.svm import SVC
from os import listdir
from flask import Flask, request
from flask import jsonify

def get_data(filename):
    data = load_svmlight_file(filename)
    return data[0], data[1]

def gettraindata():
    Xtrain, ytrain = get_data("data/testnew_train_25.0")
    
    return "Return Xtrain and Ytrain arrays"
