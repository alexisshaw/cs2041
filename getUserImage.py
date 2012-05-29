#!/usr/bin/python
import os

import connectToDatabase
import mimetypes
import notFound
import ok
import wsgiref
import wsgiref.handlers
import re

def getUserImage(environ, start_response):
    m = re.search('userid=([^&]*)', environ['QUERY_STRING'])
    headers = []
    status  = ''
    message = ''
    if m==None:
        return notFound.notFound(environ,start_response)

    userid = m.group(1)

    connection = connectToDatabase.connect()
    c = connection.cursor()
    c.execute("SELECT image,gender FROM users WHERE userid = %s", [userid])
    i = c.fetchone()
    c.close()
    connection.close()

    if i==None:
        return notFound.notFound(environ,start_response)
    imageData = ''

    if i[0] == None:
        if i[1] == None or i[1] == 'M':
            imageData = open (os.getcwd() + os.sep + 'anonymouse_images'
                            + os.sep + 'wikipedia_annonymous_male.png').read()
        else:
            imageData = open(os.getcwd() + os.sep + 'anonymouse_images'
                           + os.sep + 'wikipedia_annonymous_female.png').read()
    else:
        imageData = i[0]

    mime,contentEncoding = mimetypes.guess_type(imageData)

    headers = [('Content-type', str(mime))]
    if not contentEncoding == None: headers.append(('Content-encoding', str(contentEncoding)))

    message = imageData
    status  = ok.code()
    headers.append(('Content-Length', str(len(message))))
    start_response(status, headers)
    return message

wsgiref.handlers.CGIHandler().run(getUserImage)
 
