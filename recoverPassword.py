from cgi import parse_qs
import connectToDatabase
import genHTML
from login import getLoginToken, login
import ok

__author__ = 'ashaw'
def loginPage(environ, start_response):

    qs =  parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    loginFailure = False
    if ('username' in qs):
        try:
            cookie = login(qs['username'][0], qs['password'][0], True)
            start_response('303 See Other',[('Set-Cookie','login_token=%s'%cookie),('Location', connectToDatabase.getDirBase())])
            cookie =  getLoginToken(environ)
            return cookie
        except:
            loginFailure = True
    string = ''
    string += genHTML.genPageHeader('EngCupid')
    string += genHTML.genMenuBar("EngCupid", [dict(link='browse.py', name='Browse', active=True)], getLoginToken(environ))
    string += genHTML.beginContainer()
    string += """\
  <h1>Recover Password</h1>
  <form class="form-horizontal" method="GET" name='search' action="recoverPassword.py" >
    <fieldset>
      <div class="control-group">
        <label class="control-label" for="username">Username</label>
        <div class="controls">
           <input id="username" class="input-xlarge" type="text">
        </div>
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