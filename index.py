#!/usr/bin/python
from printUsers import  printUserProfiles

__author__ = 'WS02admin'

import genHTML

print genHTML.genHTTPHeader()

print genHTML.genPageHeader("EngCupid")

print genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])

print genHTML.beginContainer()

def printAlphabetChooser():


print printUserProfiles("SELECT * FROM USERS ORDER BY userid ASC WHERE userid ILIKE 'a%'")

print genHTML.endContainer()

print genHTML.genPageFooter()
