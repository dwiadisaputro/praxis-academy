import psycopg2
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

conn = psycopg2.connect(host="0.0.0.0", database="web", user="dwi", password="blkk57")
curs = conn.cursor()

@app.route("/list", methods=["GET"])
def list():
    try:
        query= f"select * from barang"
        curs.execute(query)
        result = curs.fetchall()
        print(result)
        return jsonify({
            "id": 1
        })
    except Exception as e:
        print(e)

@app.route("/add", methods=["POST"])
def add():
    try:
        payload = json.loads(request.data)
        pengirim = payload["pengirim"]
        produk = payload["produk"]
        asal = payload["asal"]
        query = f"insert into barang (pengirim, produk, asal) values ('{pengirim}', '{produk}', '{asal}')"
        # print(query)
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "berhasil"
        })
    except Exception as e:
        print(e)
if "__name__" == "__main__":
    app.run(host="0.0.0.0", port=5000)