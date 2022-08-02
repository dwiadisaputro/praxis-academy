from flask import Flask, jsonify, json, request
import psycopg2
import java.util.regex.Pattern.compile
# from flask_cors import CORS


app = Flask (__name__)
# # cors = CORS(app, resources={r'/read/*' : {'origins': 'http://localhost:3000'}})
# # CORS(app, resources={r"/api/*":{"origins":"*"}})
# app.config['CORS HEADERS'] = 'Content-Type'
# resp.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
# CORS(app)



# @app.route("/")
# def helloWorld():
#     return "Hello, cross-origin-world! 222"

conn = psycopg2.connect(host="0.0.0.0", database="project", user="project", password="blkk57")
curs = conn.cursor()

@app.route("/read", methods=["GET"])
# @cross_origin(origins=['http://localhost:3000'])
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
        
fun main() {
    val myEmail = "abc.de@mail.com"
    val otherEmail = "abc.com"
    val emailRegex = compile(
        "[a-zA-Z0-9\\+\\.\\_\\%\\-\\+]{1,256}" +
                "\\@" +
                "[a-zA-Z0-9][a-zA-Z0-9\\-]{0,64}" +
                "(" +
                "\\." +
                "[a-zA-Z0-9][a-zA-Z0-9\\-]{0,25}" +
                ")+"
    )

    val isMyEmailValid = emailRegex.matcher(myEmail).matches()
    val isOtherEmailValid = emailRegex.matcher(otherEmail).matches()

    println("Email $myEmail is $isMyEmailValid")
    println("Email $otherEmail is $isOtherEmailValid")
}

# =================================
# @app.route("/read1", methods=["GET"])
# def list1():
#     try:
#         query = f"select * from form"
#         curs.execute(query)
#         result = curs.fetchall()
        
#         data = []
#         for i in result:
#             data.append({
#                 "form_id": i[0],
#                 "organizationName": i[1],
#                 "country": i[2],
#                 "province": i[3],
#                 "city": i[4],
#                 "address": i[5],
#                 "currency": i[6],
#                 "language": i[7]
#             })
#         return jsonify({
#             "data": data
#         })
#     except Exception as e:
#         print(e)
##======================

@app.route("/upload", methods=["POST"])
def upload():
    try:
        payload = json.loads(request.data)
        username = payload["username"]
        password = payload["password"]
        query = f"insert into register (username, password) values ('{username}', '{password}')"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "berhasil memasukkan data baru",
            "data": "register"
        }), 200
    except Exception as i:
        return jsonify({
            "message": "gagal memasukkan data",
            "error": f"{i}"
        }), 400

if "__name__" == "__main__":
    app.run(host="0.0.0.0", port=5000)
    

