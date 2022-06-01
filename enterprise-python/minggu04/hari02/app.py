from flask import Flask, request
from flask_mongoengine import MongoEngine
app = Flask(__name__)

app.config["MONGODB_SETTINGS"]-[
    "host": "mongodb://localhost/mahasiswa"
]
db = MongoEngine(app)

class biodata(db.Document):
    name = db.StringField(max_length = 150)
    address = db.Dictfield()
    
@app.route('/')
def welcomeUser():
    return "Welocome to my base"

@app.route('/create_student', methods=["POST"])
def creatStuden():
    data = request.json
    student = Student(**data).save()
    return student.to_json()

if __name__ == "__main__":
    app.run()