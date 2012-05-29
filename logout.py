#!/usr/bin/python
import connectToDatabase
import login
import wsgiref.handlers

def loginPage(environ, start_response):
    login.logout(login.getLoginToken(environ))
    start_response('303 See Other',[('Location', connectToDatabase.getDirBase())])
    return ''

if __name__ == "__main__":
    wsgiref.handlers.CGIHandler().run(loginPage)
