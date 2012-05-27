#!/usr/bin/python

__author__ = 'WS02admin'

import genHTML
import sys
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
      <div class="page-header">
          <h1>%(userid)s</h1>
      </div>
   </div>
   <div class="row">
      <div class="span3">
         <table class="table table-condensed table-striped">
            <tbody>
""" % l
from datetime import date

l['age'] = (date.today() - l['dob']).days/365
print """
               <tr>
                  <td class="muted">Age </td>
                  <td>%(age)s</td>
""" % l
if not (l['age_wanted_low'] == None and l['age_wanted_high'] == None):
    if l['age_wanted_low'] == None:
        l['age_wanted_low'] = ''
    if l['age_wanted_high'] == None:
        l['age_wanted_high'] = ''
    print """\
                  <td>%(age_wanted_low)s - %(age_wanted_high)s</td>
""" % l
else:
    print """\
                  <td></td>
"""
print """\
               </tr>
"""


if not(l['gender'] == None and l['gender_wanted'] == None):
    if l['gender'] == None:
        l['gender'] = ''
    if l['gender_wanted'] == None:
        l['gender_wanted'] = ''
    print """\
               <tr>
                  <td class="muted">Gender </td>
                  <td>%(gender)s</td>
                  <td>%(gender_wanted)s</td>
               </tr>
""" % l

if not(l['height'] == None and\
    l['height_wanted_low'] == None and\
    l['height_wanted_high'] == None):
    if l['height'] == None:
        l['height'] = ''
    else:
        l['height'] = str(l['height']) + ' <span class="muted">m</span>'
    print """
               <tr>
                  <td class="muted">Height</td>
                  <td>%(height)s</td>
""" % l
    if l['height_wanted_low'] == None and \
       l['height_wanted_high'] == None:
        print """\
                  <td></td>
"""
    else:
        if l['height_wanted_low'] == None:
            l['height_wanted_low'] = ''
        else:
            l['height_wanted_low'] = str(l['height_wanted_low']) + ' <span class="muted">m</span>'
        if l['height_wanted_high'] == None:
            l['height_wanted_high'] = ''
        else:
            l['height_wanted_high'] = str(l['height_wanted_high']) + ' <span class="muted">m</span>'
        print """\
                  <td>%(height_wanted_low)s - %(height_wanted_high)s</td>
"""
    print """\
               </tr>
"""

if not(l['weight'] == None and\
    l['weight_wanted_low'] == None and\
    l['weight_wanted_high'] == None):
    if l['weight'] == None:
        l['weight'] = ''
    else:
        l['weight'] = str(l['weight']) + ' <span class="muted">kg</span>'
    print """\
               <tr>
                  <td class="muted">Weight</td>
                  <td>%(weight)s</td>
""" % l
    if l['weight_wanted_low'] == None and \
       l['weight_wanted_high'] == None:
        print """\
                  <td></td>
"""
    else:
        if l['weight_wanted_low'] == None:
            l['weight_wanted_low'] = ''
        else:
            l['weight_wanted_low'] = str(l['weight_wanted_low']) + ' <span class="muted">kg</span>'
        if l['weight_wanted_high'] == None:
            l['weight_wanted_high'] = ''
        else:
            l['weight_wanted_high'] = str(l['weight_wanted_high']) + ' <span class="muted">kg</span>'
        print """\
                  <td>%(weight_wanted_low)s - %(weight_wanted_high)s</td>
"""
    print """\
               </tr>
"""
print """
               <tr>
                  <td class="muted">Editor</td>
                  <td>%(editor)s</td>
                  <td>%(editor_wanted)s</td>
               </tr>
""" % l
print """
            </tbody>
         </table>
      </div>
      <div class="span6">
         <table class = "table table-condensed table-striped">
            <tbody>
"""
print """
               <tr>
                  <td class="muted">Engineering Discipline</td>
                  <td>%(engineering_discipline)s</td>
                  <td>%(engineering_discipline_wanted)s</td>
               </tr>
""" % l
print """
               <tr>
                  <td class="muted">Favorite Star Wars Movie</td>
                  <td>%(favorite_star_wars_movie)s</td>
                  <td>%(favorite_star_wars_movie_wanted)s</td>
               </tr>
""" %l
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
