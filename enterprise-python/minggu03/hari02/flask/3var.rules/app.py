from flask import Flask
app = Flask(__name__)

@app.route('/')
def nama():
    return'Sugeng rawuh'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}'

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return f'blog number {postID}'

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return f'Revision Number {revNo}'

@app.route('/flask')
def hello_flask():
    return 'Hello flask, ini percoban'

@app.route('/python/')
def hell_python():
    return 'Hello python, ini sekedar percobaan tampilan'

if __name__ == '__main__':
    app.run(debug = True)