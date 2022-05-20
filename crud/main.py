from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient
import os
import pprint

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
# print(password)
connection_string = f"mongodb+srv://dwi:{password}@cluster0.ylbba.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

mydb = client["mydb"]
mycol = mydb["riwayat"]

datalist = [{'nama':'samosir', 'age':27, 'alamat':'sulawesi'}, {'nama':'zaki', 'age':20, 'alamat':'jawa'}, 
            {'nama':'syafak', 'age':19, 'alamat':'rembang'}, {'nama':'ike', 'age':22, 'alamat':'pati'}]
mycol.insert_many(datalist)