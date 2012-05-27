#!/usr/bin/python
import wsgiref.handlers
import notFound
import ok
from printUsers import getUserProfiles, countUserProfiles
from cgi import parse_qs

__author__ = 'WS02admin'

import genHTML

#print genHTML.genHTTPHeader()

def printAlphabetChooser():
    return 'a'


def printPage(environ, start_response):
    qs = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    pagenum = qs['pagenum'] if qs['pagenum'] != None and qs['pagenum'].isdigit else 0
    search = (qs['search'] if qs['search'] != None else '')

    responseCode = ok.code()

    string = ''
    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])
    string += genHTML.beginContainer()
    if pagenum > (countUserProfiles('a', '', '%')-1)/10 or not qs['search'].isdigit:
        responseCode = notFound.code()
        string += "<div class='span12'><div class=\"hero-unit\"><H1>404 :(</H1><p>Sorry but that page seems not to exist</p></div></div>"
    else:
        string += getUserProfiles('a', '', '%', 10, pagenum)
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(responseCode, [('Content-type', 'text/html')])
    return string

wsgiref.handlers.CGIHandler().run(printPage)
