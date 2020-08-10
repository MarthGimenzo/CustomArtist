import os
import bcrypt
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from datetime import date
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_CA')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI_CA')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

# Index Page Route


@app.route('/', methods=['POST', 'GET'])
def index():
    if 'artistname' in session:
        return render_template('artist_index.html')

    elif 'clientname' in session:
        return render_template('client_index.html')

    return render_template('index.html')

# ARTIST SIDE
# Registering as new artist


@app.route('/register_artist', methods=['POST', 'GET'])
def register_artist():
    if request.method == 'POST':
        artists = mongo.db.artists
        existing_artist = artists.find_one({'username':
                                           request.form['artistname']})

        if existing_artist is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'),
                                     bcrypt.gensalt())
            artists.insert({'username': request.form['artistname'],
                            'password': hashpass,
                            'phone': request.form['phone']})
            session['artistname'] = request.form['artistname']
            all_assignments = list(mongo.db.assignments.find())
            return render_template('artist_index.html',
                                   assignments=all_assignments)
        return render_template('register_artist.html', userexists=True)
    return render_template('register_artist.html')


# ARTIST SIDE
# Artist Login Route

@app.route('/artist_login', methods=['POST'])
def artist_login():
    artists = mongo.db.artists
    login_artist = artists.find_one({'username': request.form['artistname']})
    if login_artist:
        if bcrypt.hashpw(request.form['artistpass'].encode('utf-8'),
                         login_artist['password']) == login_artist['password']:
            session['artistname'] = request.form['artistname']
            all_assignments = list(mongo.db.assignments.find())
            return render_template('artist_index.html',
                                   assignments=all_assignments)

    print('Not Accepted')
    return render_template('index.html', badlogin=True)


@app.route('/artist_login/all_assignments')
def assignments():
    all_assignments = list(mongo.db.assignments.find())
    return render_template('artist_index.html', assignments=all_assignments)


# ARTIST SIDE
# View Details of assignment as artist


@app.route('/assignment_detail/<assignment_id>')
def assignment_details(assignment_id):
    the_assignment = mongo.db.assignments.find_one({"_id":
                                                   ObjectId(assignment_id)})
    return render_template('assignment_details.html',
                           assignment=the_assignment)


# ARTIST SIDE
# Adding a proposal

@app.route('/add_proposal/<assignment_id>')
def add_proposal(assignment_id):
    the_assignment = mongo.db.assignments.find_one({"_id":
                                                   ObjectId(assignment_id)})
    return render_template('add_proposal.html', assignment=the_assignment)


@app.route('/insert_proposal/<assignment_id>', methods=['POST'])
def insert_proposal(assignment_id):
    proposals = mongo.db.proposals
    full_insert = request.form.to_dict()

    # Add artist name to the proposal
    full_insert['artist_name'] = session['artistname']

    # Add the _id and phone of the artist's record to the proposal
    artist_insession_record = mongo.db.artists.find_one({"username":
                                                        session['artistname']})
    full_insert['artist_id'] = (artist_insession_record['_id'])
    full_insert['artist_phone'] = (artist_insession_record['phone'])

    # Add the _id of the assignment record to the proposal as assignment_id
    coupled_assignment = mongo.db.assignments.find_one({"_id":
                                                       ObjectId(assignment_id)})
    full_insert['assignment_id'] = (coupled_assignment['_id'])

    proposals.insert_one(full_insert)
    return redirect(url_for('assignments'))

# ARTIST SIDE
# Deleting a proposal


@app.route('/delete_proposal/<proposal_id>')
def delete_proposal(proposal_id):
    mongo.db.proposals.delete_one({'_id': ObjectId(proposal_id)})
    return redirect(url_for('my_proposals'))

# ARTIST SIDE
# Editing and updating a proposal


@app.route('/edit_proposal/<proposal_id>/<assignment_id>')
def edit_proposal(proposal_id, assignment_id):
    the_proposal = mongo.db.proposals.find_one({"_id": ObjectId(proposal_id)})
    all_assignments = mongo.db.assignments.find_one({"_id":
                                                    ObjectId(assignment_id)})
    return render_template('edit_proposal.html',
                           proposal=the_proposal, assignment=all_assignments)


@app.route('/update_proposal/<proposal_id>/<assignment_id>', methods=["POST"])
def update_proposal(proposal_id, assignment_id):
    proposals = mongo.db.proposals

    artist_insession_record = mongo.db.artists.find_one({"username":
                                                        session['artistname']})

    proposals.update({'_id': ObjectId(proposal_id)},
                     {'title': request.form.get('title'),
                      'description': request.form.get('description'),
                      'materials': request.form.get('materials'),
                      'availability_start':
                      request.form.get('availability_start'),
                      'availability_end': request.form.get('availability_end'),
                      'artist_name': session['artistname'],
                      'artist_id': (artist_insession_record['_id']),
                      'assignment_id': ObjectId(assignment_id)
                      })
    return redirect(url_for('my_proposals'))


# ARTIST SIDE
# Viewing proposals of the artist in session

@app.route('/my_proposals')
def my_proposals():

    # Find only proposals of the current user in session
    session_artist_proposals = list(mongo.db.proposals.find({"artist_name":
                                                            session['artistname']}))

    # Add all assigmnents so that it can be iterated through
    all_assignments = list(mongo.db.assignments.find())
    return render_template('my_proposals.html',
                           proposals=session_artist_proposals,
                           assignments=all_assignments)


# ARTIST SIDE
# Signing out as artist


@app.route('/sign_out')
def sign_out():
    session.pop('artistname')
    return redirect(url_for('index'))


# CLIENT SIDE
# Registering as a new Client


@app.route('/register_client', methods=['POST', 'GET'])
def register_client():
    if request.method == 'POST':
        clients = mongo.db.clients
        existing_client = clients.find_one({'username':
                                           request.form['clientname']})

        if existing_client is None:
            hashpass = bcrypt.hashpw(request.form['clientpass'].encode('utf-8'),
                                     bcrypt.gensalt())
            clients.insert({'username': request.form['clientname'],
                           'password': hashpass})
            session['clientname'] = request.form['clientname']
            login_client = clients.find_one({'username':
                                            session['clientname']})
            client_id = login_client['_id']
            only_user_assignments = list(mongo.db.assignments.find({'client_id':
                                         ObjectId(client_id)}))
            return redirect(url_for('my_assignments',
                                    assignments=only_user_assignments))

        return render_template('register_client.html', userexists=True)

    return render_template('register_client.html')

# CLIENT SIDE
# Client Login Route


@app.route('/client_login', methods=['POST'])
def client_login():
    clients = mongo.db.clients
    login_client = clients.find_one({'username':  request.form['clientname']})

    if login_client:
        if bcrypt.hashpw(request.form['clientpass'].encode('utf-8'),
                         login_client['password']) == login_client['password']:
            session['clientname'] = request.form['clientname']
            client_id = login_client['_id']
            return redirect(url_for('my_assignments'))
    print('Not Accepted')
    return render_template('index.html', badlogin2=True)


@app.route('/client_login/my_assignments')
def my_assignments():
    clients = mongo.db.clients
    login_client = clients.find_one({'username': session['clientname']})
    client_id = login_client['_id']
    only_user_assignments = list(mongo.db.assignments.find({'client_id':
                                                           ObjectId(client_id)}))
    return render_template('client_index.html',
                           assignments=only_user_assignments)


# CLIENT SIDE
# View Details of Client's posted assignment

@app.route('/assignment_details_client/<assignment_id>')
def assignment_details_client(assignment_id):
    the_assignment = mongo.db.assignments.find_one({"_id":
                                                   ObjectId(assignment_id)})
    coupled_proposals = list(mongo.db.proposals.find({"assignment_id":
                                                     ObjectId(assignment_id)}))
    return render_template('assignment_details_client.html',
                           assignment=the_assignment,
                           proposals=coupled_proposals)

# CLIENT SIDE
# Adding a new assignment


@app.route('/add_assignment')
def add_assignment():
    return render_template('add_assignment.html')


@app.route('/insert_assignment', methods=['POST'])
def insert_assignment():
    full_insert = request.form.to_dict()
    assignments = mongo.db.assignments

    # Add the _id of the client's record as client_id
    client_insession_record = mongo.db.clients.find_one({"username":
                                                        session['clientname']})
    full_insert['client_id'] = (client_insession_record['_id'])
    print(full_insert)

    today = date.today()
    datetoday = today.strftime("%Y-%m-%d")
    print(datetoday)
    full_insert['add_date'] = datetoday

    assignments.insert_one(full_insert)
    return redirect(url_for('my_assignments'))


# CLIENT SIDE
# Deleting an assignment

@app.route('/delete_assignment/<assignment_id>')
def delete_assignment(assignment_id):
    mongo.db.assignments.delete_one({'_id': ObjectId(assignment_id)})
    mongo.db.proposals.delete_many({'assignment_id': ObjectId(assignment_id)})
    return redirect(url_for('my_assignments'))


# CLIENT SIDE
# Signing out as Client

@app.route('/sign_out_client')
def sign_out_client():
    session.pop('clientname')
    return redirect(url_for('index'))

# Other

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
