import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix
import pickle
import gatherData
def predict(filename):
# Test the unseen mails for Spam

    train_dir = '../dataset/ling-spam/train-mails'
    dictionary = gatherData.make_Dictionary(train_dir)
    model1 = pickle.load(open("Final_NB_Model", "rb"))
    model2 = pickle.load(open("Final_SVC_Model", "rb"))
    test_dir = '../dataset/ling-spam/test-mails'
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
    #print(confusion_matrix(test_labels,result2))