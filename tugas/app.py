from flask import Flask, jsonify, request, json
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



conn = psycopg2.connect(host="0.0.0.0", database="web", user="dwi", password="blkk57")
curs = conn.cursor()

@app.route("/baca", methods=["GET"])
def list():
    try:
        query = f"select * from daftar"
        curs.execute(query)
        result = curs.fetchall()
        
        data = []
        for i in result:
            data.append({
                "id": i[0],
                "namaperusahaan": i[1],
                "email": i[2],
                "password": i[3],
                "negara": i[4],
                "alamat": i[5],
                "matauang": i[6],
                "bahasa": i[7],
                "zonaWaktu": i[8]
            })
        return jsonify({
            "data": data
        })
    except Exception as e:
        print(e)
        

@app.route("/add", methods=["POST"])
def add():
    try:
        payload = json.loads(request.data)
        namaperusahaan = payload["namaperusahaan"]
        email = payload["email"]
        password = payload["password"]
        negara = payload["negara"]
        alamat = payload["alamat"]
        matauang = payload["matauang"]
        bahasa = payload["bahasa"]
        # print(namaPerusahaan)
        query = f"insert into daftar (namaperusahaan, email, password, negara, alamat, matauang, bahasa) values ('{namaperusahaan}', '{email}', '{password}', '{negara}', '{alamat}', '{matauang}', '{bahasa}')"
        print(query)
        curs.execute(query)
        conn.commit()
        curs.close()
        conn.close()
        return jsonify({
            "message": "tambah data berhasil"
        })
    except Exception as e:
        return jsonify({
            "message": "data gagal masuk",
            "detailMessage": f"{e}"
        }), 400

@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    try:
        query = f"delete from daftar where id={id}"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message":"berhasil terhapus"
        })
    except Exception as e:
        return jsonify({
            "message":"gagal terhapus",
            "detailMessage":f"{e}"
        }), 400

@app.route("/ubah/<id>", methods=["PUT"])
def ubah(id):
    try:
        payload = json.loads(request.data)
        namaperusahaan = payload["namaperusahaan"]
        email = payload["email"]
        password = payload["password"]
        negara = payload["negara"]
        alamat = payload["alamat"]
        matauang = payload["matauang"]
        bahasa = payload["bahasa"]
        # print(namaPerusahaan)
        query = f"update daftar set namaperusahaan=('{namaperusahaan}'), email=('{email}'), password=('{password}'), negara=('{negara}'), alamat=('{alamat}'), matauang=('{matauang}'), bahasa=('{bahasa}') where id=({id})"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "ubah data berhasil",
        })
    except Exception as e:
        return jsonify({
            "message": "data gagal diubah",
            "detailMessage": f"{e}"
        }), 400

if "__name__" == "__main__":
    app.run(host="0.0.0.0", port=5000)