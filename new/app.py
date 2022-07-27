from cmath import e
from http.client import responses
from flask import Flask, jsonify, json, request
import psycopg2

app = Flask(__name__)


conn = psycopg2.connect(host="0.0.0.0", database="project", user="project", password="blkk57")
curs = conn.cursor()

@app.route("/baca", methods=["GET"])
def read():
    try:
        query = f"select * from register"
        curs.execute(query)
        result = curs.fetchall()
        data = []
        for i in result:
            data.append({
                "register_id": i[0],
                "username": i[1],
                "password": i[2]
            })
        return jsonify({
            "data": data
        })
    except Exception as e:
        print(e)


@app.route("/upload", methods=["POST"])
def upload():
    try:
        payload = json.loads(request.data)
        username = payload["username"]
        password = payload["password"]
        query = f"insert into register (username, password) values ('{username}', '{password}')"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "berhasil memasukkan data baru",
            "data": "register"
        }), 200
    except Exception as i:
        return jsonify({
            "message": "gagal memasukkan data",
            "error": f"{i}"
        }), 400

###------login----###
@app.route("/login", methods=["GET"])
def login():
    try:
        payload = json.loads(request.data)
        query = f"select a.akun_id, a.username, a.password from form where a.username = '{payload['username']}' and a.password = '{payload['password']}'"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "Berhasil Masuk"
        }), 200
    except Exception as e:
        return jsonify({
            "message": "gagal membaca",
            "error": f"{e}"
        }), 400


if "__name__"=="__main__":
    app.run(host="0.0.0.0", port=8080)