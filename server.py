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

# Connect to db
db_connect = create_engine('sqlite:///albums.db')
app = Flask(__name__)
api = Api(app)


# Create API resources
class Albums(Resource):
    def get(self):
        conn = db_connect.connect()
        query_db = conn.execute("SELECT DISTINCT album FROM album")
        result = jsonify({'album list': [i[0] for i in query_db.cursor.fetchall()]})
        return result


class Artists(Resource):
    def get(self):
        conn = db_connect.connect()
        query_db = conn.execute("SELECT DISTINCT artist FROM album")
        result = jsonify({'artists': [i[0] for i in query_db.cursor.fetchall()]})
        return result


class Artistdetails(Resource):
    def get(self, artist_name):
        conn = db_connect.connect()
        # Protect against SQL injection
        restricted_char = "!=<>*0&|"
        for char in restricted_char:
            artist_name = artist_name.replace(char, "")
        query_db = conn.execute("SELECT DISTINCT album FROM album WHERE artist='{0}'".format(artist_name.title()))
        result = jsonify({'artist album list': [i[0] for i in query_db.cursor.fetchall()]})
        return result


class Genreyear(Resource):
    def get(self):
        conn = db_connect.connect()
        query_db = conn.execute("SELECT COUNT(album) as count, year FROM album GROUP BY year ORDER BY count desc")
        result = jsonify({'genre year count': [i[0] for i in query_db.cursor.fetchall()]})
        return result


class Genrenum(Resource):
    def get(self):
        conn = db_connect.connect()
        query_db = conn.execute("SELECT genre, count(album) as count FROM album GROUP BY genre ORDER BY count desc")
        result = jsonify({'genre album count': [i[0] for i in query_db.cursor.fetchall()]})
        return result

# Create API routes
api.add_resource(Albums, '/albums')
api.add_resource(Genreyear, '/albums/yr')
api.add_resource(Genrenum, '/albums/num')

api.add_resource(Artists, '/artist')
api.add_resource(Artistdetails, '/artist/<string:artist_name>')

# Run check and port
if __name__ == '__main__':
    app.run(port='5002')
