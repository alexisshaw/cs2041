#!/usr/bin/python

import wsgiref.handlers
import genHTML

def code():
    return "404 Not Found"
def header():
    return [("Content-type", "text/html")]
def body():
    return "<H1>404 Not Found </H1>"

def notFound(environ, start_response):
    string = ''

    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='browse.py', name='Browse', active=True)])
    string += genHTML.beginContainer()
    responseCode = notFound.code()
    string += """\
        <div class='span12'>
          <div class="hero-unit">
            <H1>404 :(</H1>
            <p>Sorry but that page seems not to exist</p>
          </div>
        </div>
"""
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(responseCode, [('Content-type', 'text/html')])
    return string

if __name__ == "__main__":
    wsgiref.handlers.CGIHandler().run(notFound)