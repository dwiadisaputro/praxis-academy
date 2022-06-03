from flask import Flask, request, Response
import pymongo
import json
from bson.objectid import ObjectId
app = Flask(__name__)


try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1000)
    db = mongo.kegiatan
    mongo.server_info()
except:
    print("ERROR - tidak tersambung ke database")

########################################
##--buat database kegiatan--##
########################################
@app.route("/acara", methods=["POST"])
def create_user():
    try:
        user = {'date': request.form["date"],
                'time': request.form["time"],
                'activity': request.form["activity"]}
        dbResponse = db.acara.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(
            response = json.dumps(
                {"message": "data berhasil dibuat",
                 "id":f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="aplication/json")
    except Exception as ex:
        print("*******")
        print(ex)
        print("*******")
        

########################################
##--membaca database kegiatan--##
########################################
@app.route("/acara", methods=["GET"])
def get_some_acara():
    try:
        data = list(db.acara.find())
        for user in data:
            user["_id"]=str(user["_id"])
        return Response(
            response=json.dumps(data), status=500, mimetype="aplication/json")
    except Exception as ex:
        return Response(response=json.dumps({"message": "data gagal terbaca"}),status=500, mimetype="aplication/json")

# ########################################
# ##--memperbarui database kegiatan--##
# ########################################
@app.route("/acara/<id>", methods=["PATCH"])
def update_user(id):
    try:
        dbResponse=db.acara.update_one(
            {"_id": ObjectId(id)},
            {"$set":{"date": request.form["date"]}}
        )
        if dbResponse.modified_count ==1:
            return Response(
                response=json.dumps({"message":"data diperbarui"}),
                status=200, mimetype="aplication/json")
            return Response(
                response=json.dumps({"message":"tidak ada yang diperbarui"}),
                status=200, mimetype="aplication/json")
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "maaf data gagal diperbarui"}),
            status=500, mimetype="aplication/json")

# ########################################
# ##--menghapus data kegiatan--##
# ########################################
@app.route("/acara/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.acara.delete_one({"_id":ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps({"message":"data telah terhapus", "id":f"{id}"}),
                status=200, mimetype="aplication/json")
        return Response(
            response=json.dumps({"message":"data tidak ditemukan", "id":f"{id}"}),
            status=200, mimetype="aplication/json")
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message":"maaf data tidak terhapus"}),
            status=500, mimetype="aplication/json")

########################################

########################################
if __name__=="__main__":
    app.run(debug=True)