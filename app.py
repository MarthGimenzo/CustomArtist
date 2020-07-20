import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

MONGO_CA = os.environ['MONGO_CA']
MONGO_URI_CA = os.environ['MONGO_URI_CA']

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)