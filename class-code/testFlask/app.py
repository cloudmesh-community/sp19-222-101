from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'SUCC GUH YEET FAM SQUAD HELLA LIT AF DAB'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
