"""
Main module of the server file
"""

from flask import Flask, render_template, request
import connexion
import os


# Create the application instance
app = connexion.App(__name__, specification_dir="./")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def savePort():
   portFile = open('./savedFiles/port.txt', 'w')
   portFile.write(str(myPort))
   portFile.close()


myPort = 8080
savePort()


# Read the yaml file to configure the endpoints
app.add_api("master.yml")

# create a URL route in our application for "/"
@app.route("/")
def home():
   return render_template("home.html")

def method_not_allowed(e):
   return render_template("error.html", port=myPort)

app.add_error_handler(405, method_not_allowed)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=myPort, debug=False)
