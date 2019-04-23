from flask import Flask, jsonify
import connexion

app = connexion.App(__name__, specification_dir="./")

app.add_api("cpu.yaml")

@app.route('/')

def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)

if( __name__ == "__main__"):
    app.run(host="0.0.0.0", debug=True, port=5000)

