from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import json
 
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"
 
DB_HOST = "localhost"
DB_NAME = "web"
DB_USER = "dwi"
DB_PASS = "blkk57"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/')
def Index():
    # return render_template('index.html')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM students"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)
 
@app.route('/add', methods=['POST'])
def add_student():
    connection = psycopg2.connect(host="localhost:5432", database="web", user="dwi", password="blkk57")
    cursor = connection.cursor()
    try:
        payload = json.loads(request.data)
        fname = payload['fname']
        lname = payload['lname']
        email = payload['email']
        
        query = f"INSERT INTO students(fname, lname, email) values ('{fname}','{lname}','{email}')"
        
        cursor.execute(query)
        connection.commit()
        return jsonify({
            "message":"berhasil",
            "response":"terkirim"
        })
    except Exception as x:
        print("........")
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # if request.method == 'POST':
    #     fname = request.form['fname']
    #     lname = request.form['lname']
    #     email = request.form['email']
    #     cur.execute("INSERT INTO students (fname, lname, email) VALUES (%s,%s,%s)", (fname, lname, email))
    #     conn.commit()
    #     flash('Student Added successfully')
    #     return redirect(url_for('Index'))
 
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    try:
        payload = json.loads(request.data)
        fname = payload['fname']
        lname = payload['lname']
        email = payload['email']
        
        query = f"INSERT INTO students(fname, lname, email) values ('{fname}','{lname}','{email}')"
        
        # cursor.execute(query)
        # connection.commit()
        return jsonify({
            "message":"berhasil",
            "response":"terkirim"
        })
    except Exception as x:
        print("........")
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # cur.execute('SELECT * FROM students WHERE id = %s', (id))
    # data = cur.fetchall()
    # cur.close()
    # print(data[0])
    # return render_template('edit.html', student = data[0])
 
@app.route('/update/<id>', methods=['POST'])
def update_student(id):
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE students
            SET fname = %s,
                lname = %s,
                email = %s
            WHERE id = %s
        """, (fname, lname, email, id))
        flash('Student Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_student(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM students WHERE id = {0}'.format(id))
    conn.commit()
    flash('Student Removed Successfully')
    return redirect(url_for('Index'))
 
if __name__ == "__main__":
    app.run(debug=True)