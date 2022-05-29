from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<html><body><h1>Selamat Datang</h1></body></html>'

##---- ini akan tampil (heloo nama !)--##
# @app.route('/')
# def index():
#     return render_template('hello.html')

# @app.route('/hello/<user>')
# def hello_name(user):
#     return render_template('hello.html', name = user)


##---ini akan tampil, jika scorenya >50 ; hasilnya Fail, jika <50 maka hasilnya Pass--##
@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello.html', marks = score)

@app.route('/hasil')
def hasil():
    dict = {'matgs':70, 'phy':60, 'kom':80}
    return render_template('hasil.html', hasil = dict)


if __name__ == '__main__':
    app.run(debug = True)