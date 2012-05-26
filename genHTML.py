__author__ = 'WS02admin'

def genHTTPHeader():
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

      <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
      <style>
        body{
          padding-top:60px;
        }
      </style>
      <link href="bootstrap/css/bootstrap-responsive.min.css" rel="stylesheet">
  </head>
  <body>
""" % {'title': title}

def genMenuBar(title, links):
    menuString = """\
    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="brand" href="EngCupid.py">%(title)s</a>
          <div class="nav-collapse">
            <ul class="nav">
""" % {'title':title}
    for l in links:
        menuString += ("""\
              <li %(activeClass)s><a href=\"%(link)s\">%(name)s</a></li>""") \
            % {'link': l['link'],'name':l['name'], 'activeClass':'class="active"' if l['active'] else ''}
    menuString += """\
            </ul>
            <form action="" class="navbar-search pull-right">
              <input type="text" placeholder="Search" class="search-query span2">
            </form>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
"""
    return menuString;

def beginContainer():
    return '    <div class="container">\n'

def endContainer():
    return '    </div>\n'

def genPageFooter():
    return """\
    <script src="js/jquery.min.js"></script>
    <script src="bootstrap/js/bootstrap.min.js"></script>
  </body>
</html>
"""
