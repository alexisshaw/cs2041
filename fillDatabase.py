import glob
import os
import connectToDatabase

from createTables import createTables
from createTables import dropTables
from parseUser import parseUser

__author__ = 'WS02admin'

connection = connectToDatabase.connect()
c = connection.cursor()

dropTables(c)
createTables(c)
connection.commit()

path = 'users'+os.sep



for dir in sorted(glob.glob(os.path.join(path,'*'))):
    if os.path.isdir(dir):
        parseUser(connection, dir)

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
c.close()
connection.commit()
connection.close()
