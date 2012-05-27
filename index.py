#!/usr/bin/python
import wsgiref.handlers
import notFound
import ok
from printUsers import getUserProfiles, countUserProfiles
from cgi import parse_qs
#import cgitb; cgitb.enable()
__author__ = 'WS02admin'

import genHTML

def printAlphabetChooser():
    return 'a'


def printPage(environ, start_response):
    string = ''
    qs =  parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    excepted = False
    try:
        if 'pagenum' in qs:
            pagenum = int(qs['pagenum'][0])
        else:
            pagenum = 0 
    except:
        pagenum = 0
        excepted = True 
    try:
        search = qs['browse'][0]
    except:
        search = ''
    responseCode = ok.code()

    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])
    string += genHTML.beginContainer()
    if excepted or pagenum > (countUserProfiles(search, '', '%')-1)/10 and countUserProfiles(search, '', '%')!= 0:
        string += genHTML.genPagination((countUserProfiles(search, '', '%') - 1)/10, environ['SCRIPT_NAME']+environ['SCRIPT_INFO']+'?browse='+search, pagenum)
        responseCode = notFound.code()
        string += "<div class='span12'><div class=\"hero-unit\"><H1>404 :(</H1><p>Sorry but that page seems not to exist</p></div></div>"
    else:
        if countUserProfiles(search, '', '%') == 0:
            string +=  "<div class='span12'><div class=\"hero-unit\"><H1>No Results Found</H1><p>We're sorry but there are no users that meet your search criteria</p></div></div>"
        string += getUserProfiles(search, '', '%', 10, pagenum)
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(responseCode, [('Content-type', 'text/html')])
    return string

wsgiref.handlers.CGIHandler().run(printPage)
