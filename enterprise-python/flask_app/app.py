from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 20017, username='dwiadisaputro', password='blk57')

db = client.flask_db
todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')