#!/usr/bin/python
from printUser import getGenderRowString, getFavoriteStarWarsMovieRowString, getAgeRowString, getHeightRowString, getWeightRowString, getEditorRowString, getEngineeringDisciplineRowString

__author__ = 'WS02admin'

import genHTML
import connectToDatabase

print genHTML.genHTTPHeader()

print genHTML.genPageHeader("EngCupid")

print genHTML.genMenuBar("EngCupid", [dict(link='EngCupid.py', name='Home', active=True)])

print genHTML.beginContainer()


conn = connectToDatabase.connect(dictCon = True)
c    = conn.cursor()
c.execute("SELECT * FROM USERS ORDER BY userid DESC LIMIT 1")
l = c.fetchone()
c.close()
conn.close()

print """
<div class="row">
   <div class="span3">
      <div class="thumbnail">
         <img src = "getUserImage.py?userid=%(userid)s" \>
      </div>
   </div>
   <div class="span9">
      <h2>%(userid)s</h2>
      <hr>
   </div>
   <div class="row">
      <div class="span3">
         <table class="table table-condensed table-striped">
            <tbody>
""" % l

print getAgeRowString(l)
print getGenderRowString(l)
print getHeightRowString(l)
print getWeightRowString(l)
print getEditorRowString(l)

print """\
             </tbody>
         </table>
      </div>
      <div class="span6">
         <table class="table table-condensed table-striped">
            <tbody>
"""

print getEngineeringDisciplineRowString(l)
print getFavoriteStarWarsMovieRowString(l)
print """
            </tbody>
         </table>
      </div>
   </div>
</div>
<hr>
"""


print genHTML.endContainer()

print genHTML.genPageFooter()
