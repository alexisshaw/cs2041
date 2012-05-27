#!/usr/bin/python
import wsgiref
import ok
from printUsers import getUserProfiles, countUserProfiles

__author__ = 'WS02admin'

import genHTML

print genHTML.genHTTPHeader()

def printAlphabetChooser():
    return 'a'


def printPage(environ, start_response):
    string = ''
    string += genHTML.genPageHeader("EngCupid")
    string += genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])
    string += genHTML.beginContainer()
    string += countUserProfiles('a', '', '%')
    string += getUserProfiles('a', '', '%', 10, 0)
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(ok.code(), [('Content-type', 'text/html')])
    return string

wsgiref.handlers.CGIHandler().run(printPage)
