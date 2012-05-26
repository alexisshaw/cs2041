#!/usr/bin/python
import connectToDatabase

def getUserImage(environ, start_response):
    connection = connectToDatabase.connect();

    c = connection.cursor();
    c.execute("SELECT image from table where userid = %s", )
