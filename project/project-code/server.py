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



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
