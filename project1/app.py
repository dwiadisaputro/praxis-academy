from flask import Flask, jsonify, json, make_response, request
import psycopg2, os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/read/*": {"origin": "*"}})



conn = psycopg2.connect(host="0.0.0.0", database="project", user="project", password="blkk57")
curs = conn.cursor()




##-------database form----##
@app.route("/baca", methods=["GET"])
def baca():
    try:
        query = f"select * from form"
        curs.execute(query)
        result = curs.fetchall()
        data = []
        for i in result:
            data.append({
                "form_id": i[0],
                "organizationName": i[1],
                "country": i[2],
                "province": i[3],
                "city": i[4],
                "address": i[5],
                "postalCode": i[6],
                "currency": i[7],
                "language": i[8]
            })
        return jsonify({
            "data": data
        })
    except Exception as e:
        print(e)


@app.route("/tambah", methods=["POST"])
def tambah():
    try:
        payload = json.loads(request.data)
        organizationname = payload["organizationname"]
        country = payload["country"]
        province = payload["province"]
        city = payload["city"]
        address = payload["address"]
        postalcode = payload["postalcode"]
        currency = payload["currency"]
        language = payload["language"]
        query = f"insert into form (organizationname, country, province, city, address, postalcode, currency, language) values ('{organizationname}', '{country}', '{province}', '{city}', '{address}', '{postalcode}', '{currency}', '{language}')"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "data berhasil ditambahkan"
        }), 200
    except Exception as e:
        return jsonify({
            "message": "data gagal ditambahkan",
            "error": f"{e}"
        }), 400

@app.route("/ubah/<id>", methods=["PUT"])
def ubah(id):
    try:
        payload = json.loads(request.data)
        organizationname = payload["organizationname"]
        username = payload["username"]
        email = payload["email"]
        password = payload["password"]
        country = payload["country"]
        province = payload["province"]
        city = payload["city"]
        address = payload["address"]
        postalcode = payload["postalcode"]
        currency = payload["currency"]
        language = payload["language"]
        query = f"update form set organizationname=('{organizationname}'), username=('{username}'), email=('{email}'), password=('{password}'), country=('{country}'), province=('{province}'), city=('{city}'), address=('{address}'), postalcode=('{postalcode}'), currency=('{currency}'), language=('{language}') where form_id=({id})"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "data berhasil dirubah"
        }), 200
    except Exception as e:
        return jsonify({
            "message": "data gagal dirubah",
            "error": f"{e}"
        }), 400
        
@app.route("/hapus/<id>", methods=["DELETE"])
def hapus(id):
    try:
        query = f"delete from form where form_id={id}"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "data berhasil terhapus"
        }), 200
    except Exception as e:
        return jsonify({
            "message": "data gagal terhapus",
            "erroe": f"{e}"
        }), 400
##-------form selesai----##





##-----akun---##
@app.route("/read", methods=["GET"])
@cross_origin(allow_headers=['Content-Type'])
def cross_origin_json_get():
    auth = request.authorization
    try:
        query = f"select * from akun"
        curs.execute(query)
        result = curs.fetchall()
        data = []
        for i in result:
            data.append({
                "akun_id": i[0],
                "email": i[1],
                "password": i[2]
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
        email = payload["email"]
        password = payload["password"]
        query = f"insert into akun (email, password) values ('{email}', '{password}')"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "data berhasil ditambahkan"
        }), 200
    except Exception as e:
        return jsonify({
            "message": "data gagal ditambahkan",
            "error": f"{e}"
        }), 400

@app.route("/ganti/<id>", methods=["PUT"])
def ganti(id):
    try:
        payload = json.loads(request.data)
        email = payload["email"]
        password = payload["password"]
        query = f"update akun set email=('{email}'), password=('{password}') where akun_id=({id})"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "data berhasil dirubah"
        }), 200
    except Exception as e:
        return jsonify({
            "message": "data gagal dirubah",
            "error": f"{e}"
        }), 400


@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    try:
        query = f"delete from akun where akun_id={id}"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "data berhasil terhapus"
        }), 200
    except Exception as e:
        return jsonify({
            "message": "data gagal terhapus",
            "erroe": f"{e}"
        }), 400





if "__name__"=="__main__":
    app.run(debug=True)