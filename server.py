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
# root
class Api(Resource):
    def get(self):
        return "Please read the READ ME.md for instructions on how to use this Album API"


# Returns all distinct albums
class Albums(Resource):
    def get(self):
        conn = db_connect.connect()
        query_db = conn.execute("SELECT DISTINCT album FROM album")
        result = jsonify({'albumList': [i[0] for i in query_db.cursor.fetchall()]})
        return result


# Returns all distinct artists
class Artists(Resource):
    def get(self):
        conn = db_connect.connect()
        query_db = conn.execute("SELECT DISTINCT artist FROM album")
        result = jsonify({'artistList': [i[0] for i in query_db.cursor.fetchall()]})
        return result


# CRUD operation endpoints for albums
class Artistdetails(Resource):
    def get(self, artist_name):
        conn = db_connect.connect()
        # Protect against SQL injection
        restricted_char = "!=<>*0&|/\\"
        for char in restricted_char:
            artist_name = artist_name.replace(char, "")
        query_db = conn.execute("SELECT DISTINCT album FROM album WHERE artist='{0}'".format(artist_name.title()))
        result = jsonify({'artistAlbumList': [i[0] for i in query_db.cursor.fetchall()]})
        return result

    def put(self, artist_name, album_name, album_name_new):
        conn = db_connect.connect()
        # Protect against SQL injection
        restricted_char = "!=<>*0&|/\\"
        for char in restricted_char:
            artist_name = artist_name.replace(char, "")
        query_db = conn.execute("UPDATE album SET album='{0}' WHERE artist='{1}' AND"
                                " album='{2}'".format(artist_name.title(), album_name.title(), album_name_new.title()))
        result = jsonify({'putAlbumId': [i[0] for i in query_db.cursor.fetchall()]})
        return result, 201

    def post(self, artist_name, album_name):
        conn = db_connect.connect()
        # Protect against SQL injection
        restricted_char = "!=<>*0&|/\\"
        for char in restricted_char:
            artist_name = artist_name.replace(char, "")
        query_db = conn.execute("INSERT INTO album (album, artist) VALUES"
                                " ({0},{1})".format(artist_name.title(), album_name.title()))
        result = jsonify({'postAlbumId': [i[0] for i in query_db.cursor.fetchall()]})
        return result, 201

    def delete(self, artist_name, album_name):
        conn = db_connect.connect()
        # Protect against SQL injection
        restricted_char = "!=<>*0&|/\\"
        for char in restricted_char:
            artist_id = artist_name.replace(char, "")
            album_id = album_name.replace(char, "")
        query_db = conn.execute("DELETE FROM album WHERE"
                                " artist_id='{0}' AND album_id='{1}'".format(artist_name, album_name)
                                )
        result = jsonify({'deleteAlbumId': [i[0] for i in query_db.cursor.fetchall()]})
        return result, 204


# Returns album count by year
class Genreyear(Resource):
    def get(self):
        conn = db_connect.connect()
        query_db = conn.execute("SELECT year, COUNT(album) as album_count FROM album GROUP BY year ORDER BY"
                                " album_count desc")
        result = jsonify({'genreYearCount': [dict(zip(tuple(query_db.keys()), i)) for i in query_db.cursor]})
        return result


# Returns album count by genre
class Genrenum(Resource):
    def get(self):
        conn = db_connect.connect()
        query_db = conn.execute("SELECT genre, COUNT(album) as album_count FROM album GROUP BY genre ORDER BY"
                                " album_count desc")
        result = jsonify({'genreAlbumCount': [dict(zip(tuple(query_db.keys()), i)) for i in query_db.cursor]})
        return result

# Create API routes
api.add_resource(Api, '/')

api.add_resource(Albums, '/albums')

api.add_resource(Artistdetails, '/albums/<string:artist_name>/<string:album_name>/<string:album_name_new>')

api.add_resource(Genreyear, '/albums/yr')
api.add_resource(Genrenum, '/albums/genre')

api.add_resource(Artists, '/artists')

# Run check and port
if __name__ == '__main__':
    app.run(port='5002')
