from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg':'Hello World'})

@app.route('/information', methods=['POST'])
def send_information():
    url = request.json['url']
    headline = request.json['headline']
    message = request.json['message']
    return jsonify({'msg':message,'info':'True'})
# Run Server

if __name__ == '__main__':
    app.run(debug=True)
