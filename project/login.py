from flask import Flask, redirect, request, session, flash
import bcrypt
import werkzeug
import psycopg2

app = Flask(__name__)
app.secret_key = "membuatLoginFlask1"

conn = psycopg2.connect(host="0.0.0.0", database="project", user="project", password="blkk57")
curs = conn.cursor()

@app.route('login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        query = f"select * from register where (username, password) values ('{email}', '{password}')"
        curs.execute(query)
        user = curs.fetchall()
        conn.commit()
        
        if user is not None and len(user) > 0 :
            if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
                session['name'] = user ['name']
                session['email'] = user['email']
                return redirect()
            else:
                flash("gagal, email dan password tidak cocok")
                return ()
        else:
            flash("gagal, user tidak ditemukan")
            return ()
    else:
        return()
        
        
@app.route('/register', methods=["POST", "GET"])
        

if __name__ == '__main__':
    app.run(debug=True)