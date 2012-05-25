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
<title>{title}</title>
</head>

<body>
"""

def getPageFooter():
    return """\
</body>
</html>
"""