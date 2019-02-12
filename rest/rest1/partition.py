import requests
import numpy as np
from sklearn.externals.joblib import Memory
from sklearn.datasets import load_svmlight_file
from sklearn.svm import SVC
from os import listdir
from flask import Flask, request

def data_partition(filename, ratio):
    file = open(filename,'r')
    training_file=filename+'_train_'+str(ratio)
    test_file=filename+'_test_'+ str(ratio)
    data = file.readlines()
    count = 0
    size = len(data)
    ftrain =open(training_file,'w')
    ftest =open(test_file,'w')
    for line in data:
        if(count< int(size*ratio)):
            ftrain.write(line)
        else:
            ftest.write(line)
        count = count + 1  

def partition(filename,ratio):
    ratio = float(ratio)
    path='data/'+filename
    data_partition(path,ratio)
    return "Successfully Partitioned"
