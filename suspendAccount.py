#!/usr/bin/python

import string
import connectToDatabase
import genHTML
import login
import wsgiref.handlers
import forbidden

__author__ = 'ashaw'
def deleteAccount(environ, start_response):
    wasloggedin = login.isLoggedIn(login.getLoginToken(environ))

    conn = connectToDatabase.connectToDatabase()
    c = conn.cursor()
    c.execute("UPDATE FROM users SET account_status = 'Suspended' WHERE userid = %s", [login.getUserId(login.getLoginToken(environ))])
    conn.commit()
    c.close()
    conn.close()

    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='browse.py', name='Browse', active=True)], login.getLoginToken(environ))
    string += genHTML.beginContainer()
    if wasloggedin:
        string += """\
            <div class='span12'>
              <div class="hero-unit">
                <H1>Account Suspended</H1>
                <p>Your account has been suspended.</p>
              </div>
            </div>
    """
    else:
        return forbidden.forbidden(environ,start_response)
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(ok.code(), [('Content-type', 'text/html')])
    return string

if __name__ == "__main__":
    wsgiref.handlers.CGIHandler().run(deleteAccount)