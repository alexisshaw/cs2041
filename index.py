#!/usr/bin/python
from printUsers import  printUserProfiles

__author__ = 'WS02admin'

import genHTML

print genHTML.genHTTPHeader()

print genHTML.genPageHeader("EngCupid")

print genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])

print genHTML.beginContainer()

def printAlphabetChooser():
    return 'a'

def escape(search):
    return search.replace('`','``').replace('_','`_').replace('%','`%')

searchstring = 'a'
print printUserProfiles("SELECT * FROM USERS WHERE userid ILIKE %s ESCAPE '`' ORDER BY userid ASC ", [escape(searchstring)+'%'])

print genHTML.endContainer()

print genHTML.genPageFooter()
