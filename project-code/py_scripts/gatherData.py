from flask import Flask, render_template, request
from pathlib import Path
import os
import pickle
import py_scripts
import py_scripts.trainer as trainer


##################################################################
##################################################################
### This function retrieves the file from the input on the web ###
### browser, and saves it to a file in the 'user_input_files   ###
### directory. It then calls predict() to get the prediction.  ###
### RETURNS: html template to render, along with variables for ###
###          the html file.                                    ###
##################################################################
##################################################################
def upload():
    #####################################
    ### Retrieve file from user_input ###
    #####################################
    
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, '../user_input_files/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    filename = ""
    fileCounter = 0
    for file in request.files.getlist("file"):
        
        filename = file.filename
        #################################
        ### Remove any existing files ###
        #################################
        for my_file in os.listdir(target):
            file_path = os.path.join(target, my_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
        fileCounter+=1
        file.save(os.path.join(target, filename))

    portFile = open(str(APP_ROOT)+'/../savedFiles/port.txt', 'r')
    port = int(portFile.read())

    if(fileCounter<1):
        return(render_template("error.html", port=port))
    ##############################################################
    ### Call predict to get prediction and other usefule info. ###
    ##############################################################
    result, svm_conf, description, dict_words, dict_nums = trainer.predict(filename)
    var1 = svm_conf[0]
    var2 = svm_conf[1]
    var3 = svm_conf[2]
    var4 = svm_conf[3]
    total = var1+var2+var3+var4
    conf_matr_values = [var1, var2, var3, var4]

    nb_scores, svm_scores = findScores()

    for i in range(0,4):
      nb_scores[i] = round(nb_scores[i], 2)
    for i in range(0,4):
      svm_scores[i] = round(svm_scores[i], 2)

    path = os.path.dirname(os.path.abspath(__file__))

    

    # Remove user input file
    os.remove(str(path)+'/../user_input_files/'+filename)
    

    return render_template("showModel.html", prediction=result, 
    filename=filename, conf_matr_values=conf_matr_values, 
    total=total, description=description, scores=svm_scores, port=port)



################################################################
################################################################
### This function finds the accuracy, precision, recall, and ###
### f1 score of the model.                                   ###
################################################################
################################################################
def findScores():
  path = os.path.dirname(os.path.abspath(__file__))
  with open(path+'/../savedFiles/NB_Conf_Matr', 'rb') as handle:
      nb_conf = pickle.loads(handle.read())
  with open(path+'/../savedFiles/SVM_Conf_Matr', 'rb') as handle:
    svm_conf = pickle.loads(handle.read())

  nb_tp = nb_conf[3]
  nb_tn = nb_conf[0]
  nb_fp = nb_conf[1]
  nb_fn = nb_conf[2]
  nb_tot = nb_tp+nb_tn+nb_fp+nb_fn

  svm_tp = svm_conf[3]
  svm_tn = svm_conf[0]
  svm_fp = svm_conf[1]
  svm_fn = svm_conf[2]
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

