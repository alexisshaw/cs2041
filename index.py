#!/usr/bin/python
from printUsers import getUserProfiles, countUserProfiles

__author__ = 'WS02admin'

import genHTML

print genHTML.genHTTPHeader()

print genHTML.genPageHeader("EngCupid")

print genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])

print genHTML.beginContainer()

def printAlphabetChooser():
    return 'a'

print countUserProfiles('a','','%')
print getUserProfiles('a', '','%', 10 , 0)

print genHTML.endContainer()

print genHTML.genPageFooter()
