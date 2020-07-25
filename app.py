import os
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ['MONGO_CA']
app.config['MONGO_URI'] = os.environ['MONGO_URI_CA']
app.secret_key = os.environ['SECRET_KEY']

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')

@app.route('/login')
def login():
    return 'You are a banana'

@app.route('/register_artist', methods=['POST', 'GET'])
def register_artist():
    if request.method == 'POST':
        artists = mongo.db.artists
        existing_artist = artists.find_one({'username' : request.form['username']})

        if existing_artist == None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            artists.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'
    
    print('Hello, You!')
    return render_template('register_artist.html')

    return 'You are a mango' 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)