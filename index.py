#!/usr/bin/python
from printUser import  getUserBioSummaryString
from printUsers import fetchAdditionalProfileInfo

__author__ = 'WS02admin'

import genHTML
import connectToDatabase

print genHTML.genHTTPHeader()

print genHTML.genPageHeader("EngCupid")

print genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])

print genHTML.beginContainer()


conn = connectToDatabase.connect(dictCon = True)
users    = conn.cursor()
internalCursor = conn.cursor()
users.execute("SELECT * FROM USERS ORDER BY userid ASC")

for user in users:
    l = user
    l = fetchAdditionalProfileInfo(l, internalCursor)
    print  getUserBioSummaryString(l)

internalCursor.close()
users.close()
conn.close()

print genHTML.endContainer()

print genHTML.genPageFooter()
