from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')
db = client.mydatabase

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    db.mycol.insert_one(data)
    return 'Data inserted successfully!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
