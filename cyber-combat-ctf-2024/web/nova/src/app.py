from flask import Flask, redirect, request, render_template, jsonify, make_response, abort, flash, url_for, session

app = Flask(__name__)
app.secret_key = 'bubble'

# A dictionary to hold registered users
# TODO: Set up a database for users
users = {
    'admin': 'WC4XISiEdQU8'
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
            session['username'] = username  # Storing username in session
            return redirect('/dashboard')
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

    return render_template('register.html', error=error, success=success)

# Define the dashboard endpoint, which displays the user's dashboard
@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in by checking the session
    if 'username' not in session:
        return redirect('/login')
    username = session['username']
    return render_template('dashboard.html', username=username)

# Define the logout endpoint, which logs the user out by clearing the session and redirecting to the login page
@app.route('/logout', methods=['POST'])
def logout():
    # Clear the session and redirect to the login page
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
