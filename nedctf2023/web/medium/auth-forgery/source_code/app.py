from flask import Flask, redirect, request, render_template, jsonify, make_response, abort, flash, url_for
import jwt, re
from urllib.parse import urlparse
import socket

profile_pictures = {

    'admin': 'https://mobimg.b-cdn.net/v3/fetch/62/624e27fde335d49e2dd3c6b75c6027a3.jpeg'

}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F)rrkmmZW#(@Bt%yf7grRUxD'

# A dictionary to hold registered users

# TODO: Set up a database for users

users = {
    'admin': 'k79J%H79%ykW',
    'kid': '*4J8df3$VrTx',
    'luffy': 'X80y6@iZb21l',
    'law': 'X80y6@iZb21l',
    'shanks': 'NCC{au7h_th3n_$$rf}'
}


def authenticate_user(username, password):
    if username in users and users[username] == password:
        return True
    return False


# Define the home endpoint, which redirects to /login
@app.route('/')
def home():
    return redirect('/login')


# Define the login endpoint, which displays the login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            jwt_token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
            response = make_response(redirect('/api/token?username={}'.format(username)))
            response.set_cookie('JWT', jwt_token)
            return response
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)


# Define the registration endpoint, which displays the registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    success = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Register the user

        if username in users:
            return render_template('register.html', error='Username already taken')

        users[username] = password

        # Show a success message and redirect the user to the login page
        return render_template('register.html', success='Registration successful')
        
       # success = 'Registration successful! You can now log in with your new account.'

    return render_template('register.html', error=error, success=success)


# Define the dashboard endpoint, which displays the user's dashboard
@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in by verifying the JWT token in the cookie
    token = request.cookies.get('JWT')
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = payload['username']
        profile_picture = profile_pictures.get(username)
    except (jwt.exceptions.InvalidTokenError, KeyError):
        return redirect('/login')
    
    return render_template('dashboard.html', username=username, profile_picture=profile_picture)



# Define the API endpoint that returns the JWT token
@app.route('/api/token')
def get_token():
    username = request.args.get('username')
    if not username:
        return jsonify(error='Missing username'), 400

    # Check if the user exists and generate a JWT token for them
    
    # Generate a JWT token for the user
    # payload = {'username': username}
    token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
    
    # Set the token as a cookie and redirect to the dashboard
    response = make_response(redirect('/dashboard'))
    response.set_cookie('JWT', token)
    return response


# Define the logout endpoint, which logs the user out by deleting the JWT cookie and redirecting to the login page
@app.route('/logout', methods=['POST'])
def logout():
    # Delete the JWT cookie and redirect to the login page
    response = make_response(redirect('/login'))
    response.delete_cookie('JWT')
    return response


@app.route('/api/users')
def get_users():
    
    if request.remote_addr != '127.0.0.1':
        abort(403)

    response = make_response(jsonify(users))
    return response

# set the profile picture in admin panel

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
    profile_picture = request.form.get("profile_picture_url")
    token = request.cookies.get('JWT')
    if not token:
        flash('You are not logged in.', 'error')
        return redirect(url_for('login'))
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = payload['username']
        
        # Validate profile picture URL
        if not re.match(r'^https?://[^\s/$.?#].[^\s]*$', profile_picture):
            flash('Invalid URL. Only "http" and "https" protocols are allowed.', 'error')
            return redirect(url_for('dashboard'))

        # Filter out URLs with IP address in the domain name
        domain = urlparse(profile_picture).hostname
        if is_valid_ip(domain):
            flash('Invalid URL. IP address in domain name is not allowed.', 'error')
            return redirect(url_for('dashboard'))

        profile_pictures[username] = profile_picture
        flash('Profile picture updated successfully!', 'success')
    except jwt.ExpiredSignatureError:
        flash('Token expired. Please log in again.', 'error')
        return redirect(url_for('login'))
    except (jwt.InvalidTokenError, KeyError):
        flash('Invalid token. Please log in again.', 'error')
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

def is_valid_ip(address):
    try:
        socket.inet_aton(address)
        return True
    except socket.error:
        return False



if __name__ == '__main__':
    app.run(host='0.0.0.0')