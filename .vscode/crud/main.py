from dotenv import load_env, find_env
from pymongo import MongoClient
import os
import pprint
load_env(find_env())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://dwi:{password}@cluster0.ylbba.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)








# if __name__=="main":
    