from flask import Flask, session, render_template, request, redirect, g, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('user', None)
        
        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('protected'))
    
    return render_template('login.html')

@app.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html', user=session['user'])
    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user = None
    
    if 'user' in session:
        g.user = session['user']
        
@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return render_template('login.html')
#     return render_template('index.html')

# @app.route('/login', methods =['GET', 'POST'])
# def login():
#     error = None
    
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or \
#             request.form['password'] != '1234':
#             error = 'username dan password anda salah. silahkan ulangi kembali'
            
#         else:
#             flash('Selamat, anda berhasil masuk')
#             return redirect(url_for('index'))
    
#     return render_template('login.html', error = error)



if __name__ == "__main__":
    app.run(debug = True)