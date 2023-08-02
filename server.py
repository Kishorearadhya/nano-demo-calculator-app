from flask import Flask, request, jsonify
from dataclasses import dataclass

@dataclass
class Result:
    result: int


app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    numbers = request.json
    f1=numbers['first']
    f2=numbers['second']
    response = Result(f1 + f2)
    return jsonify(response)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    number = request.json
    response = Result(number['first'] - number['second'])
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
