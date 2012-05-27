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
    if not m == None:
        userid = m.group(1)
    
        connection = connectToDatabase.connect()
        c = connection.cursor()
        c.execute("SELECT image,gender FROM users WHERE userid = %s", [userid])
        i = c.fetchone()
        c.close()
        connection.close()

        if not i == None:
            if i[0] == None:
                if i[1] == None or i[1] == 'M':
                    i[0] = open('anonymouse_image' + os.sep + 'wikipedia_annonymouse_male.png')
                else:
                    i[0] = open('anonymouse_image' + os.sep + 'wikipedia_annonymouse_female.png')
            mime,contentEncoding = mimetypes.guess_type(i[0])

            headers = [('Content-type', str(mime))]
            if not contentEncoding == None: headers.append(('Content-encoding', str(contentEncoding)))

            message = i[0]
            status  = ok.code()
        else: 
            status  = notFound.code()
            headers = notFound.header()
            message = notFound.body()
    else:
        status  = notFound.code()
        headers = notFound.header()
        message = notFound.body()
    headers.append(('Content-Length', str(len(message))))
    start_response(status, headers)
    return message

wsgiref.handlers.CGIHandler().run(getUserImage)
 