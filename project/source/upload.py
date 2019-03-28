from flask import Flask, render_template, request
import connexion
from pathlib import Path
import os

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

    return render_template("complete.html")