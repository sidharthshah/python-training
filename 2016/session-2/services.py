import json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return json.dumps({"msg": "Hello World"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
