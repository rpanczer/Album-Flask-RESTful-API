"""
API to access albums db with artist / album details
Please read the README.md for more details and instructions on use
----------------------------------------------------------
This api was tested using a Python 3.6 interpreter
Author: Bobby Panczer 8/31/2017
----------------------------------------------------------
"""

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# Connect to db
db_connect = create_engine('sqlite:///albums.db')
app = Flask(__name__)
api = Api(app)


# Create API resources
class Artists(Resource):
    def get(self):
        conn = db_connect.connect()
        query_db = conn.execute("SELECT DISTINCT artist FROM album")
        return {'artists': [i[0] for i in query_db.cursor.fetchall()]}


# Create API routes
api.add_resource(Artists, '/artists')

# Run check and port
if __name__ == '__main__':
    app.run(port='5002')
