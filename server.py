"""
API to access albums db with artist / album details
Please read the README.md for more details and instructions on use
----------------------------------------------------------
This api was tested using a Python 3.6 interpreter
Author: Bobby Panczer 8/31/2017
----------------------------------------------------------
"""
from flask import Flask, request
from flask_restful import Resource, api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

# Connect to db, assign api
db_connect = create_engine(albums.csv)
app = Flask(__name__)
app = api(app)

# Create API resources
class Collection(Resource):
    conn = db_connect.connect()
    query_db = conn.execute("select * from album")
    return {'collection': [i[0] for i in query.cursor.fetchall()]}

class Albums(Resource):
    conn = db_connect.connect()
    query_db = conn.execute("select album from album")
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return jsonify(result)

# Create API routes
api.add_resource(Collection, '/collection') # Route to artists
api.add_resource(Albums, '/albums') # Route to albums

# Run check and port
if __name__ == '__main__':
    app.run(port='5002')
