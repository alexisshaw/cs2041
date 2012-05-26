#!/usr/bin/python

__author__ = 'WS02admin'

import genHTML
import sys

print genHTML.genHTTPHeader()

print genHTML.genPageHeader("EngCupid")

print genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])

print genHTML.beginContainer()

print sys.version
print
print sys.path

print genHTML.endContainer()

print genHTML.genPageFooter()
