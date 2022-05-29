from flask import Flask, session, request, redirect, url_for
app = Flask(__name__)

# app.route('/')
# def index():
#     if 'username' in session:
#         username = session['username']
#             return 'Logged in as ' + username + '<br>' + \
#             "<b><a> href = '/Logout'>click here to log out</a></b>"
#     return "You are not logged in <br><a href = '/login'></br>" + \
#         "click here to log in</b></a>"

@app.route('/Login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))