from flask import Flask, jsonify, json, request
import psycopg2

app = Flask(__name__)

@app.route('login', methods=['GET'])
def authLogin(id):
    try:
        conn = psycopg2.connect(host="0.0.0.0", database="project", user="project", password="blkk57")
        curs = conn.cursor()
        
        payload = json.loads(request.data)
        
        query = f"select a.akun_id, a.username, a.password"
        query = f"select * from akun a join form f  on form_id = akun_id  where akun_id  = ({id})"

if __name__ == '__main__':
    app.run(debug=True)