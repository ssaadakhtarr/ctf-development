from flask import Blueprint, request, render_template, make_response, redirect, url_for, render_template_string
import jwt


web = Blueprint('web', __name__, template_folder='templates', static_folder='static')

SECRET_KEY = 'changethis'

users = {
    'admin': 'J3F1kBu!H1-x'
    }

def authenticate_user(username, password):
    if username in users and users[username] == password:
        return True
    return False


# Define the home endpoint, which redirects to /login
@web.route('/')
def home():
    return redirect('/login')


# Define the login endpoint, which displays the login form
@web.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            jwt_token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
            response = make_response(redirect('/dashboard'))
            response.set_cookie('JWT', jwt_token)
            return response
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)


# Define the registration endpoint, which displays the registration form
@web.route('/register', methods=['GET', 'POST'])
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

# @web.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         if not username.isalnum():
#             return render_template('register.html', title="Register", error="Username must be alphanumeric.")
#         token = create_jwt(username)
#         response = make_response(redirect(url_for('web.dashboard')))
#         response.set_cookie('auth_token', token)
#         return response
#     return render_template('register.html', title="Register")

@web.route('/dashboard')
def dashboard():
    # if request.args:
    #     return "Whoa there bucko, did you forget I'm not a web developer? I don't know how to handle parameters yet!"
    token = request.cookies.get('JWT')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        username = payload['username']
        
    except (jwt.exceptions.InvalidTokenError, KeyError):
        return redirect('/login')
    
    

    # test_payload = request.args.get('test')
    
    # token = request.cookies.get('auth_token')
    # user_info = decode_jwt(token)
    # print(user_info)
    # if not user_info:
    #     return redirect(url_for('web.register'))
    
    # if not str(user_info['username']).isascii():
    #     return f"It's not a pyjail XD. ASCII characters only please!"

    # restricted_stuff = [',', '[', ']', '"', "'", '_', '\\','/','headers','url','path','data','json','args','cookies','files','form','flag', '%', 'os','system','popen','sys','module','mro','class','base','getitem','subprocess','application','config','list','dict','global','builtins','import','join','first','last','reverse','lower','upper','items','format']
    restricted_stuff = ['[', ']', '_','headers','url','path','data','json','args','cookies','files','form','flag', '%', 'system','popen','sys','module','mro','class','base','application','config','list','dict','join','first','last','reverse','lower','upper','items','format', 'cp', 'os']
    
    blocked = False
    
    found_strings = []
    
    for blacklisted in restricted_stuff:
        if blacklisted in str(username):
            found_strings.append(blacklisted)
            blocked = True

    # for blacklisted in restricted_stuff:
    #     if blacklisted in str(test_payload):
    #         found_strings.append(blacklisted)
    #         blocked = True
    
    if blocked:
        title_text = "BLOCKED"
        content_html = f'''Intrusion Detected!<br>Malicious stuff: {found_strings}</br>
        '''
    else:
        title_text = f"{username}"
        content_html = "This is your dashboard incase you didn't know that."

    logout_form_html = '''
    <form action="{{ url_for('web.logout') }}" method="post">
        <input type="submit" value="Logout">
    </form>
    '''

    # dashboard_template = f'''
   
    # <div class="form-container">
    # <h1 class="welcome-text">{title_text}</h1> 
   
    # {content_html}
   
    # </div>
   
    # '''

    dashboard_template = f'''
    <!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" href="{ url_for('static', filename='style.css') }">
    <script src="https://kit.fontawesome.com/a076d05399.js"></script>
  </head>
  <body>
    
  

    
      
 
    <h1 style="text-align: center; color: white;">Welcome, { title_text }!</h1>
    <p style="text-align:center; color: white;">{content_html}</p>
 
    <br>

    

    <form method="POST" action="/logout">
      <input class="logout-button" type="submit" value="Log out">
    </form>

    <br>
  </body>
</html>
    '''
    return render_template_string(dashboard_template)
    # return render_template('dashboard.html', username=title_text)



@web.route('/logout', methods=['POST'])
def logout():
    # Delete the JWT cookie and redirect to the login page
    response = make_response(redirect('/login'))
    response.delete_cookie('JWT')
    return response