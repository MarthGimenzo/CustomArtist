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
        return render_template('artist_index.html')

    return render_template('index.html')

@app.route('/artist_login', methods=['POST'])
def artist_login():
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
            return render_template('artist_index.html', assignments=mongo.db.assignments.find())

@app.route('/artist_login')
def assignments():
    return render_template('artist_index.html', assignments=mongo.db.assignments.find())

@app.route('/assignment_detail/<assignment_id>')
def assignment_details(assignment_id):
    the_assignment = mongo.db.assignments.find_one({"_id" : ObjectId(assignment_id)})
    return render_template('assignment_details.html', assignment=the_assignment)

@app.route('/add_proposal/<assignment_id>')
def add_proposal(assignment_id):
    the_assignment = mongo.db.assignments.find_one({"_id" : ObjectId(assignment_id)})
    return render_template('add_proposal.html', assignment=the_assignment)

@app.route('/insert_proposal', methods=['POST'])
def insert_proposal():
    proposals = mongo.db.proposals
    print('Got here')
    proposals.insert_one(request.form.to_dict())
    return "Inserted proposal"

@app.route('/sign_out')
def sign_out():
    session.pop('artistname')
    return redirect(url_for('index'))

@app.route('/register_artist', methods=['POST', 'GET'])
def register_artist():
    if request.method == 'POST':
        artists = mongo.db.artists
        existing_artist = artists.find_one({'username' : request.form['artistname']})

        if existing_artist == None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            artists.insert({'username' : request.form['artistname'], 'password' : hashpass})
            session['artistname'] = request.form['artistname']
            return render_template('artist_index.html', assignments=mongo.db.assignments.find())
        
        return render_template('register_artist.html',userexists=True)
    
    print('Hello, You!')
    return render_template('register_artist.html')

    return 'You are a mango' 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)