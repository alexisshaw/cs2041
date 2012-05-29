import base64
import datetime
import re
import wsgiref
import connectToDatabase
import os
from cgi import parse_qs
import genHTML
import ok

__author__ = 'Alexis Shaw'

def login(username, password, autoLogout):
    conn = connectToDatabase.connect(dictCon=True)
    c = conn.cursor()
    c.execute("SELECT userid ,pass FROM users where userid = %s", username)
    if c is None:
        raise Exception('User Does Not Exist')
    result = c.fetchone()
    if result['pass'] != password:
        return Exception('Incorrect Password')
    random = base64.b32encode(os.urandom(20)).lower()
    while c.execute("SELECT login_token FROM logindata where login_token = %s",random != None):
        random = base64.b32encode(os.urandom(20)).lower()
    c.execute("INSERT INTO logindata values(%s,%s,NOW(),%s)", random, username,autoLogout)
    conn.commit()
    c.close()
    conn.close()
    return random

def isLoggedIn(token):
    conn = connectToDatabase.connect(dictCon=True)
    c = conn.cursor()
    q = c.execute("SELECT * FROM logindata WHERE login_token = %s", token)
    conn.commit()
    c.close()
    conn.close()
    return q is not None

def updateLogin(token):
    conn = connectToDatabase.connect(dictCon=True)
    c = conn.cursor()
    c.execute("DELETE FROM logindata WHERE (lastUsed  < CURRENT_TIMESTAMP - INTERVAL 20 MINUTE) and autoLogout")
    c.execute("UPDATE FROM logindata SET lastUsed = CURRENT_TIMESTAMP WHERE login_token = %s", token)
    conn.commit()
    c.close()
    conn.close()


def logout(token):
    conn = connectToDatabase.connect(dictCon=True)
    c = conn.cursor()
    c.execute("DELETE FROM logindata WHERE login_token = %s", token)
    conn.commit()
    c.close()
    conn.close()

def loginPage(environ, start_response):
    qs =  parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    loginFailure = False
    if ('username' in qs) and ('password' in qs):
        try:
            login(qs['username'], qs['password'], True)
            start_response('303 See Other',[('Location', connectToDatabase.getDirBase())])
            return
        except:
            loginFailure = True
    string = ''
    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='browse.py', name='Browse', active=True)])
    string += genHTML.beginContainer()
    string += """
<div class="span12">
"""
    if loginFailure:
        string += """\
  <div class="alert alert-error">
    <button class="close" data-dismiss="alert">&times;</button>
    <strong>Incorrect username or password</strong>
    You have entered a username/password combination that is not in our system, please try again
  </div>
"""
    else:
        string+= """\
  <form class="form-horizontal">
    <fieldset>
      <div class="control-group">
        <label class="control-label" for="username">Username</label>
        <div class="controls">
           <input id="username" class="input-xlarge" type="text">
        <div>
      </div>
      <div class="control-group">
        <label class="control-label" for="username" value="%(username)s">Password</label>
        <div class="controls">
           <input id="username" class="input-xlarge" type="password">
        <div>
      </div>
      <div class="form-actions">
        <button class="btn btn-primary" type="submit">Login</button>
      </div>
    </fieldset>
  </form>
""" % {'username': qs['username'] if 'username' in qs else ''}

    string += """\
</div>
"""
    string += genHTML.endContainer()
    string += genHTML.genPageFooter()
    start_response(ok.code(), [('Content-type', 'text/html')])
    return string

if __name__ == "__main__":
    wsgiref.handlers.CGIHandler().run(loginPage)