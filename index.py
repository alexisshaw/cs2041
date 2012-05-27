#!/usr/bin/python
import re
import wsgiref.handlers
import notFound
import ok
from printUsers import getUserProfiles, countUserProfiles

__author__ = 'WS02admin'

import genHTML

print genHTML.genHTTPHeader()

def printAlphabetChooser():
    return 'a'


def printPage(environ, start_response):
    m = re.search('pagenum=([^&]*)', environ['QUERY_STRING'])
    pagenum = int(m.group(1) if m != None else 0)

    responseCode = ok.code()

    string = ''
    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])
    string += genHTML.beginContainer()
    string += str(countUserProfiles('a', '', '%'))
    if pagenum > (countUserProfiles('a', '', '%')-1)/10:
        responseCode = notFound.code()
        string += "<div class='span12'><div class=\"hero-unit\"><H1>404 :(</H1><p>Sorry but that page seems not to exist</p></div></div>"
    else:
        string += getUserProfiles('a', '', '%', 10, pagenum)
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(responseCode, [('Content-type', 'text/html')])
    return string

wsgiref.handlers.CGIHandler().run(printPage)
