import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'custom_artist'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-rx4bk.mongodb.net/custom_artist?retryWrites=true&w=majority'

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)