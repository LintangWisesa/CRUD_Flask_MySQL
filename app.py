from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('lintang.yaml'))
app.config['MYSQL_HOST'] = db['host']
app.config['MYSQL_USER'] = db['user']
app.config['MYSQL_PASSWORD'] = db['pass']
app.config['MYSQL_DB'] = db['db']

mysql = MySQL(app)
CORS(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data', methods=['POST', 'GET', 'DELETE', 'PUT'])
def data():
    
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users VALUES(%s, %s)', ('Fafa', 22))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'status': 'Data posted to MySQL!'})
    
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        data = cursor.execute('SELECT * FROM USERS')
        if data > 0:
            users = cursor.fetchall()
            print (users)
            return jsonify(users)

    if request.method == 'PUT':
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE users SET name = %s, age = %s WHERE name = "Andi"', ('Alibaba', 32))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'status': 'Data updated on MySQL!'})

    else:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM users WHERE name = "Euis"')
        mysql.connection.commit()
        cursor.close()
        return jsonify({'status': 'Data deleted on MySQL!'})

if __name__ == '__main__':
    app.run(debug = True)