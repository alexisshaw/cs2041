#!/usr/bin/python

from cgi import parse_qs
import string
import connectToDatabase
import genHTML
import login
import wsgiref.handlers
import forbidden
import ok

__author__ = 'ashaw'
def deleteAccount(environ, start_response):
    loggedin = login.isLoggedIn(login.getLoginToken(environ))
    userid = ''
    qs =  parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    if loggedin:
        userid = login.getUserId(login.getLoginToken(environ))
    elif 'userid' in qs:
        userid = qs['userid']
    else:
        return forbidden.forbidden(environ,start_response)

    conn = connectToDatabase.connect()
    c = conn.cursor()
    c.execute("UPDATE FROM users SET account_status = 'Active' WHERE userid = %s", [userid])
    conn.commit()
    c.close()
    conn.close()

    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='browse.py', name='Browse', active=True)], login.getLoginToken(environ))
    string += genHTML.beginContainer()
    string += """\
            <div class='span12'>
              <div class="hero-unit">
                <H1>Account Deleted</H1>
                <p>Your account is now active.</p>
                <p><a class="btn btn-primary btn-large" href="login.py">
                 Login
                </a></p>
              </div>
            </div>
    """
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(ok.code(), [('Content-type', 'text/html')])
    return string

if __name__ == "__main__":
    wsgiref.handlers.CGIHandler().run(deleteAccount)