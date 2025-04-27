from flask import Flask, request, render_template, g
import sqlite3
import time

app = Flask(__name__)
DATABASE = 'users.db'

def waf(query):
    query = query.lower()
    blocked_words = ['where', 'in', 'order', 'regexp', 'like', ' ', 'match', 'exec', 'union', 'glob', 'join', 'hex', 'blob', 'load']
    
    for word in blocked_words:
        if word in query:
            return True
    return False

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query):
    cur = get_db().cursor()
    cur.execute(query)
    result = cur.fetchone()
    return result

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')

    if waf(username):
        return "SECURITY ALERT! Not so fast..."

    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    result = query_db(query)

    if result:
        return "Welcome!"
    else:
        return "YOU DON'T BELONG HERE!"

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
