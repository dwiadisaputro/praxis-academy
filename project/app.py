from flask import Flask, jsonify
import psycopg2
from flask_cors import CORS, cross_origin


app = Flask (__name__)
cors = CORS(app, resources={r'/read/*' : {'origins': 'http://localhost:3000'}})
# CORS(app, resources={r"/api/*":{"origins":"*"}})
# app.config['CORS HEADERS'] = 'Content-Type'



# @app.route("/")
# def helloWorld():
#     return "Hello, cross-origin-world! 222"

conn = psycopg2.connect(host="0.0.0.0", database="project", user="project", password="blkk57")
curs = conn.cursor()

@app.route("/read", methods=["GET"])
@cross_origin(origins=['http://localhost:3000'])
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
    

