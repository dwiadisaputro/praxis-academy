import collections
import pymongo
import pprint

# conn_str = "mongodb+srv://dwi:blkk57@cluster0.ylbba.mongodb.net/test"
# client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

db = pymongo.MongoClient("mongodb://localhost:27017")

#database
dbmy = db["koleksi"]

#collection
collectionmy = dbmy["rak"]

#data yg akan diinsert
data = {"rak 1" : "kamus", "judul" : "kamus bhs inggris"}

#data insert
collectionmy.insert_one(data)