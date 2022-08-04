from distutils.command.config import config
import json, datetime, jwt, os
from flask import jsonify, request
from app import responses, app

def generate():
    try:
        payload = json.loads(request.data)
        expired_at = datetime.datetime.utcnow() + datetime.timedelta(days=int(os.environ.get('TOKEN_EXPIRED_IN_DAY')))
        encoded_jwt = jwt.encode({
            "id_akun": payload["id_akun"]
            "email": payload["email"]
            "password": payload["password"]
            "exp": expired_at
        }), app.config["se"]
    

