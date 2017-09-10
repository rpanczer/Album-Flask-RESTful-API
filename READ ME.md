# Albums API
Albums API provides programmatic access to content in `albums.db`. Access is given to the full list of artists, their 
respective albums, and additional details about the albums (ie the genre of the album and the release year of the album).
A list of all endpoints is provided below; all endpoints return data in [JSON](json.org) format. 

## Prerequisites
- [pip](https://pypi.python.org/pypi/pip)
- [Python 3](https://www.python.org/)

 Python modules used (click to view documentation):
- [CSV](https://docs.python.org/2/library/csv.html)
- [sqlite3](https://docs.python.org/2/library/sqlite3.html)
- [flask](http://flask.pocoo.org/docs/0.12/)
- [flask-restful](https://flask-restful.readthedocs.io/en/latest/)
- [sqlalchemy](http://docs.sqlalchemy.org/en/latest/) 
## Endpoints
- `GET` /artists
- `GET` /albums
- `GET` /albums/yr
- `GET` /albums/genre
- `GET` /albums/:artist_name
- `PUT` /albums/:artist_name/:album_name/:new_album_name
- `POST` /albums/:artist_name/:album_name
- `DELETE` /albums/:artist_name/:album_name


