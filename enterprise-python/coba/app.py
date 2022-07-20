import psycopg2
from flask import Flask, jsonify

# app = Flask(__name__)

# conn = psycopg2.connect(host="0.0.0.0", database="web", user="dwi", password="blkk57")
# curs = conn.cursor()

# @app.route("/list", methods=["GET"])
# def list():
#     try:
#         query= f"select * from barang"
#         curs.execute(query)
#         result = curs.fetchall()
#         # print(result)
        
#         data =[]
#         for i in result:
#             data.append({
#                 "id": i[0],
#                 "pengirim": i[1],
#                 "produk": i[2],
#                 "asal": i[3]
#             })
#         return jsonify({
#             "data": data
#         })
#     except Exception as e:
#         print(e)

# @app.route("/add", methods=["POST"])
# def add():
#     try:
#         payload = json.loads(request.data)
#         pengirim = payload["pengirim"]
#         produk = payload["produk"]
#         asal = payload["asal"]
#         query = f"insert into barang (pengirim, produk, asal) values ('{pengirim}', '{produk}', '{asal}')"
#         # print(query)
#         curs.execute(query)
#         conn.commit()
#         return jsonify({
#             "message": "berhasil"
#         })
#     except Exception as e:
#         print(e)
# if "__name__" == "__main__":
#     app.run(host="0.0.0.0", port=5000)
    
app = Flask (__name__)
# CORS(app, resource={r"/*": {"origin": "*"}})

conn = psycopg2.connect(host="0.0.0.0", database="project", user="project", password="blkk57")
curs = conn.cursor()

@app.route("/read", methods=["GET"])
def list():
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

# =================================
@app.route("/read1", methods=["GET"])
def list1():
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
                "currency": i[6],
                "language": i[7]
            })
        return jsonify({
            "data": data
        })
    except Exception as e:
        print(e)

if "__name__" == "__main__":
    app.run(host="0.0.0.0", port=5000)