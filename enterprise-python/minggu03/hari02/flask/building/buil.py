from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Selamat Datang'

@app.route('/anggota/<anggota>')
def hello_anggota(anggota):
    return f'Selamat datang {anggota}'

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_adm'))
    else:
        return redirect(url_for('hello_anggota', anggota = name))
    

if __name__ == '__main__':
    app.run(debug = True)