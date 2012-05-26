import glob
import os
import sqlite3
import sys

sys.path.append(os.getcwd()+os.sep+'pg'+os.sep+'lib'+os.sep+'python'+os.sep)

import psycopg2

from createTables import createTables
from createTables import dropTables
from parseUser import parseUser

__author__ = 'WS02admin'

connection = psycopg2.connect(database = '2041ass2',
     password = 'aYGOVVSmg4MfdZLg9Q5y',
     user = 'cgiclient',
     host = 'ates466.srvr',
     port = 5432)
c = connection.cursor()

dropTables(c)
createTables(c)
connection.commit()

path = 'users'+os.sep



for dir in sorted(glob.glob(os.path.join(path,'*'))):
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
c.execute("SELECT * FROM engineering_disciplines")
print c.fetchall()
