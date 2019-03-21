"""
Main module of the server file
"""

from flask import Flask, render_template, request
import connexion
import os


# Create the application instance
app = connexion.App(__name__, specification_dir="./")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Read the yaml file to configure the endpoints
app.add_api("master.yml")

# create a URL route in our application for "/"
@app.route("/")
def home():
   return render_template("home.html")
"""@app.route("/upload", methods=['POST'])
def upload():
   target = os.path.join(APP_ROOT, 'input/')
   print(target)

   if not os.path.isdir(target):
      os.mkdir(target)

   for file in request.files.getlist("file"):
      print(file)
      filename = file.filename
      destination = "/".join([target, filename])
      print(destination)
      file.save(destination)

   return render_template("complete.html")"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
