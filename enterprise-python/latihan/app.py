##--simpel flask--##
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     data = {
#         "id": 1,
#         "nama": "ahmad"
#     }

#     return data

##-------------------------------------##

##--Routing--##
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Selamat Pagi...!!'

##----------------------------------##

##--Variabel Rules--##
from flask import Flask
# from markupsafe import escape
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

if __name__ == '__main__':
    app.run()

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return 'Subpath %s' %escape(subpath)

##------------------##

##--Unique URLs / Redirection Behavior--##
# @app.route('/projects/')
# def projects():
#     return 'Halaman awal'

# @app.route('/about')
# def about():
#     return 'Halaman perihal'

##--------------------##

##--URL Building--##
# from flask import Flask, url_for
# from markupsafe import escape

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(escape(username))

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='Adi Putra'))

##------------------##

##--HTTP Methods--##
# from flask import request


# @app.route('/login', method=['GET', 'POST'])
# def login():
#     if request.method == 'POST' :
#         return do_the_login()
#     else:
#         return show_the_login_form()
    