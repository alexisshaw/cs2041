#!/usr/bin/env python

__author__ = 'WS02admin'

import genHTML

print genHTML.geNHTTPHeader()

print genHTML.genPageHeader("EngCupid")

print genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])
print genHTML.genPageFooter()
