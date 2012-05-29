#!/usr/bin/python
import wsgiref.handlers
import ok
__author__ = 'WS02admin'

import genHTML

def printAlphabetChooser():
    return 'a'

def printPage(environ, start_response):
    responseCode = ok.code()
    string = ''
    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='browse.py', name='Browse', active=False)])
    string += genHTML.beginContainer()
    string += """\
        <div class='span12'>
          <div class="hero-unit">
            <H1>Welcome to Eng Cupid</H1>
            <p>The dating site tailor made for Engineers and Computer Scientists</p>
          </div>
        </div>
"""
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(responseCode, [('Content-type', 'text/html')])
    return string

wsgiref.handlers.CGIHandler().run(printPage)
