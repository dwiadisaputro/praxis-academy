from flask import Flask, request, Response
import pymongo
import json
from bson.objectid import ObjectId
app = Flask(__name__)

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
@app.route("/pustaka", methods=["POST"])
def creat_user():
    try:
        user = {'judul': request.form["judul"],
                'pengarang': request.form["pengarang"],
                'penerbit': request.form["penerbit"],
                'jenis': request.form["jenis"],
                'ketebalan': request.form["ketebalan"]}
        dbResponse = db.buku.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(
            response=json.dumps(
                {"message": "Data Berhasil Dibuat",
                 "id":f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="aplication/json")
    except Exception as ex:
        print(ex)
        print("Gagal terbuat")
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
@app.route("/pustaka/<id>", methods=["PATCH"])
def update_user(id):
    try:
        dbResponse=db.buku.update_one(
            {"_id": ObjectId(id)},
            {"$set":{"judul":request.form["judul"]}})
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
@app.route("/pustaka/<id>", methods=["DELETE"])
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