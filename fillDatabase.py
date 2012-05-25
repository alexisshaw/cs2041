import glob
import os
import sqlite3
from createTables import createTables
from createTables import dropTables
from parseUser import parseUser


__author__ = 'WS02admin'

connection = sqlite3.connect('EngCupid.db')

dropTables(connection)
createTables(connection)

path = 'users'+os.sep



for dir in glob.glob(os.path.join(path,'*')):
    if os.path.isdir(dir):
        parseUser(connection, dir)

c = connection.cursor()
c.execute("SELECT * FROM operating_systems")
print c.fetchall()
c.execute("SELECT * FROM star_wars_movies")
print c.fetchall()
c.execute("SELECT * FROM editors")
print c.fetchall()
c.execute("SELECT * FROM programming_languages")
print c.fetchall()
