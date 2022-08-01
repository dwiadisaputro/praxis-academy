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

##1 membuat endpoint untuk login
class LoginUser