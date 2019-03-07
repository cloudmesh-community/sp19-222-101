"""
Main module of the server file
"""

from flask import render_template
import connexion


# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("master.yml")

# create a URL route in our application for "/"
@app.route("/")
def home():
   return render_template("home.html")
@app.route("/templates/other.html")
def other():
   return render_template("other.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
