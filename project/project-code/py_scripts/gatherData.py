import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.utils import shuffle
import pickle

def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir,f) for f in os.listdir(train_dir)]    
    all_words = []       
    for mail in emails:    
        with open(mail) as m:
            for i,line in enumerate(m):
                if i == 2:  #Body of email is only 3rd line of text file
                    words = line.split()
                    all_words += words
    
    dictionary = Counter(all_words)
    newDict = Counter(all_words)

    #print(dictionary)
    # Paste code for non-word removal here(code snippet is given below)
    list_to_remove = dictionary.keys()
    for item in list_to_remove:
        if item.isalpha() == False: 
            del newDict[item]
        elif len(item) == 1:
            del newDict[item]
    dictionary = newDict.most_common(3000)
    return dictionary

def extract_features(mail_dir, dictionary): 
    files = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files),3000))
    docID = 0
    for fil in files:
      with open(fil) as fi:
        for i,line in enumerate(fi):
          if i == 2:
            words = line.split()
            for word in words:
              wordID = 0
              for i,d in enumerate(dictionary):
                if d[0] == word:
                  wordID = i
                  features_matrix[docID,wordID] = words.count(word)
        docID = docID + 1     
    return features_matrix

def train():
    # Create a dictionary of words with its frequency

    train_dir = '../dataset/ling-spam/train-mails'
    dictionary = make_Dictionary(train_dir)

    # Prepare feature vectors per training mail and its labels

    train_labels = np.zeros(702)
    train_labels[351:701] = 1
    train_matrix = extract_features(train_dir, dictionary)
    print(train_matrix)
    # Training SVM and Naive bayes classifier

    shuffle_train_matrix, shuffle_train_labels  = randomize(train_matrix, train_labels)

    model1 = MultinomialNB()
    model2 = LinearSVC()
    model1.fit(shuffle_train_matrix,shuffle_train_labels)
    model2.fit(shuffle_train_matrix,shuffle_train_labels)

    
    #pickle.dump(model1, open("Final_NB_Model", "wb"))
    #pickle.dump(model2, open("Final_SVC_Model", "wb"))

    #train_dir = '../dataset/ling-spam/train-mails'
    #dictionary = make_Dictionary(train_dir)
    #model1 = pickle.load(open("Final_NB_Model", "rb"))
    #model2 = pickle.load(open("Final_SVC_Model", "rb"))
    test_dir = '../dataset/ling-spam/test-mails'
    test_matrix = extract_features(test_dir, dictionary)
    test_labels = np.zeros(260)
    test_labels[130:260] = 1
    result1 = model1.predict(test_matrix)
    result2 = model2.predict(test_matrix)

    print("CONFUSION NB: ")
    print(confusion_matrix(test_labels, result1))
    print("CONFUSION SVM: ")
    print(confusion_matrix(test_labels, result2))
    


def randomize(features, labels):
  newF, newL = shuffle(features, labels, random_state=0)
  return newF, newL