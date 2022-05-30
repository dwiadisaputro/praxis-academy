from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return 'selamat datang'

def hello_world():
    return 'selamat pagi kawan'
app.add_url_rule('/', 'hello', hello_world)

if __name__ == '__main__':
    app.run(debug=True)