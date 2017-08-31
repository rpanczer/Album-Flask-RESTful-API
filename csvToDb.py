import csv
import sqlite3
import server

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE album (album, artist, genre, year);")

with open('albums.csv', 'rb') as album_db:
    dr = csv.DictReader(album_db)
    to_db = [(i['album'], i['artist'], i['genre'], i['year']) for i in dr]

cursor.executemany("INSERT INTO album (album, artist, genre, year) VALUES(?,?,?,?);", to_db)
connection.commit()
connection.close()

if __name__ == '__main__':
    server()


