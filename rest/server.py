"""
Main module of the server file
"""

from flask import jsonify
import connexion


# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("cpu.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)

@app.route("/prime/<n_str>")
def isPrime(n_str):
    n = int(n_str)
    if(n<2):
        return n_str + " is not a prime number"
    is_prime = True
    for i in range(2, n):
        if n%i == 0:
            is_prime = False
    if(is_prime):
        return n_str + " is a prime number"
    else:
        return n_str + " is not a prime number"

@app.route("/add/<n1>&<n2>")
def add(n1, n2):
    return n1 + " + " + n2 + " = " + str(int(n1)+int(n2))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
