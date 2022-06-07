from flask import Flask, request, Response, render_template
import pymongo
import json
from bson.objectid import ObjectId
app = Flask(__name__)

# @app.route("/")
# def route_pustaka():
#     return render_template('awal.html')

###########################
##--connect to database
###########################
try:
    mongo=pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db=mongo.kepustakaan
    mongo.server_info()
except:
    print("ERROR - tidak terhubung ke database")
###########################
##--buat database kepustakaan
###########################
@app.route("/daftar", methods=["POST"])
def creat_user():
    try:
        pyload = json.loads(request.data)
        # user = {'judul': request.form["judul"],
                # 'pengarang': request.form["pengarang"],
                # 'penerbit': request.form["penerbit"],
                # 'jenis': request.form["jenis"],
                # 'ketebalan': request.form["ketebalan"]}
        dbResponse = db.buku.insert_one(pyload)
        print(dbResponse.inserted_id)
        return Response(
            response=json.dumps(
                {"message": "Data Berhasil Dibuat",
                 "id":f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="aplication/json")
    except Exception as ex:
        return Response(response=json.dumps({"message":"Gagal terbuat"}), status=200, mimetype="aplication/json")
###########################
##--membaca data
###########################
@app.route("/pustaka", methods=["GET"])
def get_some_pustaka():
    try:
        data = list(db.buku.find())
        for user in data:
            user["_id"]=str(user["_id"])
        return Response(
            response=json.dumps(data), status=500, mimetype="aplication/json")
    except Exception as ex:
        return Response(response=json.dumps({"message": "data gagal terbaca"}),status=500, mimetype="aplication/json")
###########################
##--memperbarui database
###########################
@app.route("/terbaru/<id>", methods=["PATCH"])
def update_user(id):
    try:
        dbResponse=db.buku.update_one(
            {"_id": ObjectId(id)},
            {"$set":{"Judul":request.form["Judul"]}},
            {"$set":{"Pengarang":request.form["Pengarang"]}},
            {"$set":{"tahunTerbit":request.form["tahunTerbit"]}},
            {"$set":{"jenisBuku":request.form["jenisBuku"]}},
            {"$set":{"Ketebalan":request.form["Ketebalan"]}},)
        if dbResponse.modified_count ==1:
            return Response(
                response=json.dumps({"message":"telah diperbarui"}),
                status=200, mimetype="aplication/json")
        return Response(
            response=json.dumps({"message":"tidak ada data yang diperbarui"}),
            status=200, mimetype="aplication/json")
    except Exception as ex:
        return Response(
            response=json.dumps({"message":"Maaf data gagal dirubah"}),
            status=500, mimetype="aplication/json")
###########################
##--hapus data
###########################
@app.route("/hapus/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse=db.buku.delete_one({"_id":ObjectId(id)})
        if dbResponse.deleted_count ==1:
            return Response(
                response=json.dumps({"message":"Data telah terhapus", "id":f"{id}"}),
                status=200, mimetype="aplication/json")
        return Response(
            response=json.dumps({"message":"Data telah terhapus", "id":f"{id}"}),
            status=200, mimetype="aplication/json")
    except Exception as ex:
        return Response(
            response=json.dumps({"message":"Maaf data gagal terhapus"}),
            status=500, mimetype="aplication/json")
###########################
##--test
###########################
if __name__ == "__main__":
    app.run(debug=True)