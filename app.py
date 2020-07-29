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

@app.route('/', methods=['POST', 'GET'])
def index():
    if 'artistname' in session:
        return 'You are logged in as ' + session['artistname']

    return render_template('index.html')
    

@app.route('/login', methods=['POST'])
def login():
    print('Got to Login')
    
    artists = mongo.db.artists
    print(artists)
    login_artist = artists.find_one({'username' : request.form['artistname']})
    print('Got here3')
    print(login_artist)
    if login_artist:
        if bcrypt.hashpw(request.form['artistpass'].encode('utf-8'), login_artist['password']) == login_artist['password']:
            print('Accepted')
            session['artistname'] = request.form['artistname']
            return 'You are logged in as ' + session['artistname']


@app.route('/register_artist', methods=['POST', 'GET'])
def register_artist():
    if request.method == 'POST':
        artists = mongo.db.artists
        existing_artist = artists.find_one({'username' : request.form['artistname']})

        if existing_artist == None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            artists.insert({'username' : request.form['artistname'], 'password' : hashpass})
            session['artistname'] = request.form['artistname']
            return redirect(url_for('index'))
        
        return render_template(
            'register_artist.html',
            userexists=True
)
    
    print('Hello, You!')
    return render_template('register_artist.html')

    return 'You are a mango' 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)