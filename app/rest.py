import pymysql
from app import app
from db import mysql
from flask import Flask, jsonify, request

@app.route('/persons/list', methods=['GET'])
def persons():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    request.method == 'GET'

    cursor.execute("SELECT * FROM persons")
    conn.commit()
    

    rows = cursor.fetchall()        
    resp = jsonify(rows)
    resp.status_code = 200
    return resp


@app.route('/persons', methods=['POST'])
def persons_post():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    request.method == 'POST'

    cursor.execute ('insert into persons (name, address) values ("Fabian Lopez", "prof.fabian.lopez@gmail.com") ')
    conn.commit()

    cursor.execute("SELECT * FROM persons")
    conn.commit()
    
    rows = cursor.fetchall()
    resp = jsonify(rows)
    resp.status_code = 200

    return resp


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')