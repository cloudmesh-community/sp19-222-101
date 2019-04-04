from flask import Flask, render_template, request
import numpy as np
import connexion
from pathlib import Path
import os
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
        with open(mail, encoding="latin-1") as m:
            for i,line in enumerate(m):
                if i == 2:  #Body of email is only 3rd line of text file
                    words = line.split()
                    all_words += words
    dictionary = Counter(all_words)
    newDict = Counter(all_words)

    # Remove unwanted words/letters/symbols
    list_to_remove = dictionary.keys()
    for item in list_to_remove:
        if item.isalpha() == False: 
            del newDict[item]
        elif len(item) == 1:
            del newDict[item]
    dictionary = newDict.most_common(3000)
    return dictionary

def extract_features(mail_dir, dictionary, num_files): 
    files = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files),3000))
    docID = 0
    labels = np.zeros(len(files))
    index = 0
    for fil in files:
      with open(fil, encoding="latin-1") as fi:
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
      names = fil.split('/')
      names.reverse()
      filename = names[0]
      if('spm' in filename or 'spam' in filename):
          labels[index] = 1
      index += 1 
    return features_matrix, labels

def train():

    path = os.path.dirname(os.path.abspath(__file__))
    '''# Create a dictionary of words with its frequency
    train_dir = 'dataset/train-mails/'
    dictionary = make_Dictionary(train_dir)

    with open(path+'/dictionary.txt', 'wb') as handle:
      pickle.dump(dictionary, handle)

    # Prepare feature vectors per training mail and its labels
    train_matrix, train_labels = extract_features(train_dir, dictionary, 4908)

    # Shuffle data
    shuffle_train_matrix, shuffle_train_labels  = randomize(train_matrix, train_labels)

    # Training SVM and Naive bayes classifier
    model1 = MultinomialNB()
    model2 = LinearSVC()
    model1.fit(shuffle_train_matrix,shuffle_train_labels)
    model2.fit(shuffle_train_matrix,shuffle_train_labels)

    with open(path+'/Final_NB_Model', 'wb') as handle:
      pickle.dump(model1, handle)
    with open(path+'/Final_SVM_Model', 'wb') as handle:
      pickle.dump(model2, handle)'''
    
    with open(str(path)+'/dictionary.txt', 'rb') as handle:
      dictionary = pickle.loads(handle.read())

    model1 = pickle.load(open(str(path)+"/Final_NB_Model", "rb"))
    model2 = pickle.load(open(str(path)+"/Final_SVM_Model", "rb"))
    
    # Testing and showing confusion matrices
    test_dir = 'dataset/test-mails'
    test_matrix, test_labels = extract_features(test_dir, dictionary, 1226)
    
    result1 = model1.predict(test_matrix)
    result2 = model2.predict(test_matrix)

    nb_conf_matr = confusion_matrix(test_labels, result1)
    svm_conf_matr = confusion_matrix(test_labels, result2)

    print("CONFUSION NB: ")
    print(nb_conf_matr)
    print("CONFUSION SVM: ")
    print(svm_conf_matr)

    with open(path+'/NB_Conf_Matr', 'wb') as handle:
      pickle.dump(nb_conf_matr, handle)
    with open(path+'/SVM_Conf_Matr', 'wb') as handle:
      pickle.dump(svm_conf_matr, handle)
    
    


def randomize(features, labels):
    newF, newL = shuffle(features, labels, random_state=0)
    return newF, newL

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

    result, svm_conf, description = predict(filename)
    var1 = svm_conf[0][0]
    var2 = svm_conf[0][1]
    var3 = svm_conf[1][0]
    var4 = svm_conf[1][1]
    total = var1+var2+var3+var4
    conf_matr_values = [var1, var2, var3, var4]
    nb_scores, svm_scores = findScores()
    for i in range(0,4):
      nb_scores[i] = round(nb_scores[i], 2)
    for i in range(0,4):
      svm_scores[i] = round(svm_scores[i], 2)
    



    return render_template("showModel.html", prediction=result, 
    filename=filename, conf_matr_values=conf_matr_values, 
    total=total, description=description, nb_scores=svm_scores)

def predict(filename):

    path = os.path.dirname(os.path.abspath(__file__))

    with open(str(path)+'/dictionary.txt', 'rb') as handle:
      dictionary = pickle.loads(handle.read())

    with open(str(path) + '/NB_Conf_Matr', 'rb') as handle:
      nb_conf = pickle.loads(handle.read())
    with open(str(path) + '/SVM_Conf_Matr', 'rb') as handle:
      svm_conf = pickle.loads(handle.read())

    model1 = pickle.load(open(str(path)+"/Final_NB_Model", "rb"))
    model2 = pickle.load(open(str(path)+"/Final_SVM_Model", "rb"))
    
    
    pred_dir = str(path)+'/user_input_files'
    pred_matrix, do_not_use_this_var = extract_features(pred_dir, dictionary, 1)
    result_num = model2.predict(pred_matrix)
    result = ""
    if(result_num==1):
      result = "Spam"
      description = \
      "Your email has been classified as spam because it contains" + \
      " words that are often used in spam emails."  
    else:
      result = "Ham"
      description = \
      "Your email has been classified as ham becuase it does not" + \
      " contain enough words used in spam emails to be classified" + \
      " as spam."

    os.remove(str(path)+'/user_input_files/'+filename)

    return result, svm_conf, description
        
'''def saveDictionary():
  path = os.path.dirname(os.path.abspath(__file__))
  train_dir = str(path)+'/dataset/ling-spam/train-mails/'
  dictionary = make_Dictionary(train_dir)
  print(dictionary)

  with open(str(path)+'/dictionary.txt', 'wb') as handle:
    pickle.dump(dictionary, handle)
  return

def saveConfMatr():
  path = os.path.dirname(os.path.abspath(__file__))
  with open(str(path)+'/dictionary.txt', 'rb') as handle:
    dictionary = pickle.loads(handle.read())

    model1 = pickle.load(open(str(path)+"/Final_NB_Model", "rb"))
    model2 = pickle.load(open(str(path)+"/Final_SVC_Model", "rb"))
    test_dir = str(path)+'/dataset/ling-spam/test-mails'
    test_matrix = extract_features(test_dir, dictionary)
    test_labels = np.zeros(260)
    test_labels[130:260] = 1
    result_test = model1.predict(test_matrix)
    #result2 = model2.predict(test_matrix)
    nb_conf = confusion_matrix(test_labels, result_test)

    with open(str(path)+'/confusion_matrix.txt', 'wb') as handle:
      pickle.dump(nb_conf, handle)'''

def findScores():
  path = os.path.dirname(os.path.abspath(__file__))
  with open(path+'/NB_Conf_Matr', 'rb') as handle:
      nb_conf = pickle.loads(handle.read())
  with open(path+'/SVM_Conf_Matr', 'rb') as handle:
    svm_conf = pickle.loads(handle.read())

  nb_tp = nb_conf[1][1]
  nb_tn = nb_conf[0][0]
  nb_fp = nb_conf[0][1]
  nb_fn = nb_conf[1][0]
  nb_tot = nb_tp+nb_tn+nb_fp+nb_fn

  svm_tp = svm_conf[1][1]
  svm_tn = svm_conf[0][0]
  svm_fp = svm_conf[0][1]
  svm_fn = svm_conf[1][0]
  svm_tot = svm_tp+svm_tn+svm_fp+svm_fn

  nb_acc = (nb_tp+nb_tn)/nb_tot
  svm_acc = (svm_tp+svm_tn)/svm_tot

  nb_prec = nb_tp/(nb_tp+nb_fp)
  svm_prec = svm_tp/(svm_tp+svm_fp)

  nb_rec = nb_tp/(nb_tp+nb_fn)
  svm_rec = svm_tp/(svm_tp+svm_fn)

  nb_f1 = 2*((nb_prec*nb_rec)/(nb_prec+nb_rec))
  svm_f1 = 2*((svm_prec*svm_rec)/(svm_prec+svm_rec))

  nb_scores = [nb_acc, nb_prec, nb_rec, nb_f1]
  svm_scores = [svm_acc, svm_prec, svm_rec, svm_f1]

  return nb_scores, svm_scores

  #print("NB:")
  #print("\tAcc: ", nb_acc)
  #print("\tPrec: ", nb_prec)
  #print("\tRec: ", nb_rec)
  #print("\tF1: ", nb_f1)

  #print("SVM:")
  #print("\tAcc: ", svm_acc)
  #print("\tPrec: ", svm_prec)
  #print("\tRec: ", svm_rec)
  #print("\tF1: ", svm_f1)
  


