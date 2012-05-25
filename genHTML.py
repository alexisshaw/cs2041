__author__ = 'WS02admin'

def getHTTPHeader():
    header ="""\
Content-Type: text/html

"""
    return header

def getPageHeader(title):
    return """\
<!DOCTYPE html>
<html>
<head>
<title> %(title)s</title>
</head>

<body>
""" % {'title': title}

def getPageFooter():
    return """\
</body>
</html>
"""