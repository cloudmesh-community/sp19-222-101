from flask import Flask, render_template, request
import numpy as np
import connexion
from pathlib import Path
import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix
import pickle
import gatherData
#import predict

def upload():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'user_input_files/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        
        path = Path().absolute()
        exists = os.path.isfile(str(path)+ '/user_input_files/' + filename)
        i=0
        nameNoExt = filename.replace('.txt','')
        while(exists):
            print("File exists")
            nameNoExt = filename.replace('.txt', '')
            fullpath = str(path) + '/user_input_files/' + nameNoExt + str(i) + '.txt'
            print("NEW FILE: " + fullpath)
            fullpath = fullpath.strip()
            exists = os.path.isfile(fullpath)
            print("File " + fullpath + " exists: " + str(exists))
            i = i+1
        if(i==0):
                filename = nameNoExt + '.txt'
        else:
            filename = nameNoExt + str(i-1) + '.txt'
        destination = ''.join([target, filename])
        print("FINAL DEST: " + destination)
        file.save(destination)
        print("No more files found")


        '''if exists:
            print("File exists")
            nameNoExt = filename.replace('.txt', '')
            print("NameNoExt: " + nameNoExt)
            i = 0
            print("NEW FILE: " + str(path) + '/user_input_files/'+ nameNoExt + str(i) + '.txt')
            exists = os.path.isfile(str(path) + '/' + nameNoExt+str(i)+'.txt')
            print(exists)
            while(exists):
                print("File ", str(i), " exists")
                #filename = nameNoExt + str(i) + '.txt'
                i = i+1
                exists = os.path.isfile(str(path)+'/'+nameNoExt+str(i)+'.txt')
            filename = nameNoExt + str(i) + '.txt'
            print("Final filename: " + filename)
        else:
            print("File not found")'''
        #destination = "".join([target, filename])
        #print(destination)
        #file.save(destination)

    result = predict()

    return render_template("showModel.html", prediction=result)

    def predict():
        train_dir = '../dataset/ling-spam/train-mails'
        dictionary = gatherData.make_Dictionary(train_dir)
        model1 = pickle.load(open("Final_NB_Model", "rb"))
        model2 = pickle.load(open("Final_SVC_Model", "rb"))
        '''test_dir = '../dataset/ling-spam/test-mails'
        test_matrix = gatherData.extract_features(test_dir, dictionary)
        test_labels = np.zeros(260)
        test_labels[130:260] = 1
        result1 = model1.predict(test_matrix)
        result2 = model2.predict(test_matrix)



        print("Result1: ", result1)
        print("Result2: ", result2)
        nb_conf = confusion_matrix(test_labels, result1)
        svm_conf = confusion_matrix(test_labels, result2)
        #print(confusion_matrix(test_labels,result1))
        #print(confusion_matrix(test_labels,result2))'''
        pred_dir = '../user_input_files'
        pred_matrix = gatherData.extract_features(pred_dir, dictionary)
        result1 = model1.predict(pred_matrix)
        result2 = model2.predict(pred_matrix)

        return result1