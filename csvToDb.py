"""
Converts a csv file to sqlite db then runs the api
"""
import csv
import sqlite3

connection = sqlite3.connect('albums.db')
c = connection.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS album (album TEXT, artist TEXT, genre TEXT, year TEXT);")


def data_entry():
    with open('albums.csv', 'rt') as album_db:
        dr = csv.DictReader(album_db)
        to_db = [(i['album'], i['artist'], i['genre'], i['year']) for i in dr]
        c.executemany("INSERT INTO album (album, artist, genre, year) VALUES(?,?,?,?);", to_db)

create_table()
data_entry()

connection.commit()
c.close()
connection.close()





