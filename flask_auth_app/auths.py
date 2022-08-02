## import library flask dan lainnya
from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, Api


## import PyJWT
import jwt
import datetime


## import library untuk membuat decorator
from functools import wraps

##inisialisasi object flask dkk
app = Flask(__name__) #flask
api = Api(app) #restfull
app.config['SECRET_KEY'] = "inirahasia"

##1 membuat endpoint untuk login
class LoginUser(Resource):
    def post(self):
        ##butuh multipart form untuk tranmisi data
        username = request.form.get('username')
        password = request.form.get('password')
        
        
        ## membuat kondisi pengecekan password
        if username and password == 'superadmin':
            ## hasilkan nomor token
            token = jwt.encode(
                {"username":username,
                 "exp":datetime.datetime.utcnow() + datetime.timedelta()
                }, app.config['SECRET_KEY'], algorithm="HS256"
            )
            return jsonify({
                "token":token,
                "msg":"Anda berhasil login"
            })
        return jsonify({"msg":"silahkan login"})

api.add_resource(LoginUser, "/api/login", methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)