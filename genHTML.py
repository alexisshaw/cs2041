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
            <form action="search.py" method="GET" name='search' class="navbar-search pull-right">
              <input type="text" name="search" placeholder="Search" class="search-query span2">
            </form>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
"""
    return menuString

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

def genPagination(noPages, base, activePage):
   string = ''
   pageNumbers = []
   if noPages > 11 and activePage - 5 >= 0:
       pageNumbers.append(0)
       pageNumbers.append(1)
       pageNumbers.append(-1)
       pageNumbers.append(activePage-2)
       pageNumbers.append(activePage-1)
   else:
       for i in range(0,activePage):
           pageNumbers.append(i)
   pageNumbers.append(activePage)
   if noPages > 11 and activePage + 6 <= noPages:
       pageNumbers.append(activePage+1)
       pageNumbers.append(activePage+2)
       pageNumbers.append(-1)
       pageNumbers.append(noPages-2)
       pageNumbers.append(noPages-1)
   else:
       for i in range(activePage + 1,noPages):
           pageNumbers.append(i)
   string += """\
<div class="pagination pagination-centred">
   <ul>
      <li %(class)s><a href="%(base)s&pagenum=%(activePageMinus1)s">&lsaquo;</a></li>
""" % {'class':'' if activePage!=0 else 'class="dissabled"', 'base':base,'activePageMinus1': str(activePage)}
   for i in pageNumbers:
      string+= """\
      <li %(class)s><a href="%(base)s&pagenum=%(i)s">%(i)s</a></li>
""" % {'class':'' if i != activePage or i>=0 else('class="dissabled"' if i <0 else'class=active'),
       'base':base, 'i': str(i + 1) if i>=0 else '&hellip;',
       }
   string += """\
      <li %(class)s><a href="%(base)s&pagenum=%(activePagePlus1)s">&rsaquo;</a></li>
    </ul>
</div>
""" % {'class':'' if activePage!=noPages-1 else 'class="dissabled"', 'base':base,'activePagePlus1': str(activePage+2)}
   return string