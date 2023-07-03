from flask import Flask, redirect, request, render_template, jsonify, make_response, abort, flash, url_for
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'REDACTED'

# A dictionary to hold registered users

# TODO: Set up a database for users

users = {
    'admin': 'REDACTED'
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
            response = make_response(redirect('/dashboard'))
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
        
    except (jwt.exceptions.InvalidTokenError, KeyError):
        return redirect('/login')
    
    return render_template('dashboard.html', username=username)


# Define the logout endpoint, which logs the user out by deleting the JWT cookie and redirecting to the login page
@app.route('/logout', methods=['POST'])
def logout():
    # Delete the JWT cookie and redirect to the login page
    response = make_response(redirect('/login'))
    response.delete_cookie('JWT')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)