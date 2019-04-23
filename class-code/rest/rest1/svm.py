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

def svm():
    Xtrain, ytrain = get_data("data/iris.scale_train")
    Xtest, ytest = get_data("data/iris.scale_test")

    clf = SVC(gamma=0.001, C=100, kernel='linear')
    clf.fit(Xtrain, ytrain)

    test_size = Xtest.shape[0]
    accuarcy_holder = []
    for i in range(0, test_size):
        prediction = clf.predict(Xtest[i])
        print("Prediction from SVM: "+str(prediction)+", Expected Label : "+str(ytest[i]))
        accuarcy_holder.append(prediction==ytest[i])

    correct_predictions = sum(accuarcy_holder)
    print(correct_predictions)
    total_samples = test_size
    accuracy = float(float(correct_predictions)/float(total_samples))*100
    print("Prediction Accuracy: "+str(accuracy))
    return "Prediction Accuracy: "+str(accuracy)
