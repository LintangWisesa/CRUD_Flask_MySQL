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

@app.route('/data', methods=['POST', 'GET'])
def data():
    
    if request.method == 'POST':
        body = request.json
        name = body['name']
        age = body['age']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users VALUES(null, %s, %s)', (str(name), str(age)))
        mysql.connection.commit()
        cursor.close()
        return jsonify({
            'status': 'Data is posted to MySQL!',
            'name': name,
            'age': age
        })
    
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        allData = []

        for i in range(len(users)):
            id = users[i][0]
            name = users[i][1]
            age = users[i][2]
            dataDict = {
                "id": id,
                "name": name,
                "age": age
            }
            allData.append(dataDict)

        return jsonify(allData)

@app.route('/data/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = %s', (id))
        users = cursor.fetchall()
        print(users)
        data = []

        for i in range(len(users)):
            id = users[i][0]
            name = users[i][1]
            age = users[i][2]
            dataDict = {
                "id": id,
                "name": name,
                "age": age
            }
            data.append(dataDict)

        return jsonify(data)

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