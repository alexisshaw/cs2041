#!/usr/bin/python
from cgi import parse_qs
import wsgiref.handlers
import connectToDatabase
import forbidden
import login
import notFound
import ok
import printUser
from printUsers import countUserProfiles, fetchAdditionalProfileInfo

__author__ = 'WS02admin'

import genHTML

def getUserInfo(query, values):
    string = ''
    conn = connectToDatabase.connect(dictCon=True)
    users = conn.cursor()
    internalCursor = conn.cursor()
    users.execute(query, values)
    l = None
    for user in users:
        l = user
        l = fetchAdditionalProfileInfo(l, internalCursor)
    internalCursor.close()
    users.close()
    conn.close()
    return l

def printPage(environ, start_response):
    if not login.isLoggedIn(login.getLoginToken(environ)):
        return forbidden.forbidden(environ,start_response)
    qs =  parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    if ('userid' in qs):
        if countUserProfiles(qs['userid'], '', '') > 0:
            l = getUserInfo("SELECT * FROM users WHERE userid = %s", [qs['userid']])
        else:
            return notFound.notFound(environ,start_response)
    else:
        return notFound.notFound(environ,start_response)
    responseCode = ok.code()
    string = ''
    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='browse.py', name='Browse', active=False)], login.getLoginToken(environ))
    string += genHTML.beginContainer()
    string += printUser.getUserProfile(l)
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(responseCode, [('Content-type', 'text/html')])
    return string

wsgiref.handlers.CGIHandler().run(printPage)
