from flask import Flask, render_template, request
import connexion
import os

def upload():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'user_input_files/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        exists = os.path.isfile("user_input_files/"+filename)

        if exists:
            print("File exists")
            filename += "2"
        else:
            print("File not found")
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")