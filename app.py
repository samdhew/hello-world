from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_name = os.environ['DB_NAME']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']

conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
    )

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name VARCHAR(50))")
conn.commit()

@app.route('/')
def hello():
    # cur.execute("INSERT INTO test_table (name) VALUES ('Alice')")
    # conn.commit()
    # cur.execute("SELECT * FROM test_table")
    # rows = cur.fetchall()
    # result = [{'id': row[0], 'name': row[1]} for row in rows]
    
    result = {"message":"Hello World"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
