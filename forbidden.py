import genHTML
import wsgiref.handlers
import login

__author__ = 'ashaw'

def code():
    return "403 Forbidden"
def header():
    return [("Content-type", "text/html")]

def forbidden(environ, start_response):
    string = ''

    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='browse.py', name='Browse', active=True)], login.getLoginToken(environ))
    string += genHTML.beginContainer()
    responseCode = forbidden.code()
    string += """\
        <div class='span12'>
          <div class="hero-unit">
            <H1>403 Forbidden</H1>
            <p>It seems that you are trying to go somewhere you shouldn't.</p>
            <p><a class="btn btn-primary btn-large" href='index.php'>
              return to EngCupid
            </a></p>
          </div>
        </div>
"""
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(responseCode, [('Content-type', 'text/html')])
    return string

if __name__ == "__main__":
    wsgiref.handlers.CGIHandler().run(forbidden)