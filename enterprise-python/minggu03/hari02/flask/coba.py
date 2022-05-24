# from flask import Flask
# app = Flask(__name__)

##-----Flask-Application-----##
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello World !, Selamat datang di halaman ini'


##-------Flask-Routing---------##
# @app.route('/hello')
# def hello():
#     return 'hello world'
# app.add_url_rule('/', 'hello', hello)


##-----Flask-Variable Rules-------##
# @app.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello %s!' % name

# if __name__ == '__main__':
#     app.run(debug = True)


##----Flask-HTTP Methods-----##
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return f'Selamat datang di halaman {name}'

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        eser = request.args.get('nm')
        return redirect(url_for('success', name = user))

if __name__ == '__main__':
    app.run(debug = True)