__author__ = 'WS02admin'

def geNHTTPHeader():
    header ="""\
Content-Type: text/html

"""
    return header

def genPageHeader(title):
    return """\
<!DOCTYPE html>
<html>
    <head>
        <title> %(title)s</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

        <link href="bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
    </head>
    <body>
""" % {'title': title}

def genMenuBar(title, links):
    menuString = """\
    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="EngCupid.py">%(title)s</a>
          <div class="nav-collapse">
            <ul class="nav">
""" % {'title':title}
    for l in links:
        menuString += ("""<li %(activeClass)s><a href=\"%(link)s\">%(name)s</a></li>""") \
            % {'link': l['link'],'name':l['name'], 'activeClass':'class="active"' if l['active'] else ''}
    menuString += """\
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
"""



def genPageFooter():
    return """\
        <script src="bootstrap/js/bootstrap.min.js"></script>
    </body>
</html>
"""