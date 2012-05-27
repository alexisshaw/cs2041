from datetime import date

__author__ = 'ashaw'

def getAgeRowString(l):
    l['age'] = (date.today() - l['dob']).days / 365
    string =  """
               <tr>
                  <td class="muted">Age </td>
                  <td>%(age)s</td>
""" % l
    if not (l['age_wanted_low'] == None and l['age_wanted_high'] == None):
        if l['age_wanted_low'] == None:
            l['age_wanted_low'] = ''
        if l['age_wanted_high'] == None:
            l['age_wanted_high'] = ''
        string += """\
                  <td>%(age_wanted_low)s - %(age_wanted_high)s</td>
""" % l
    else:
        string += """\
                  <td></td>
"""
    string += """\
               </tr>
"""
    return string


def getHeightRowString(l):
    string = ''
    if not(l['height'] == None and
           l['height_wanted_low'] == None and
           l['height_wanted_high'] == None):
        if l['height'] == None:
            l['height'] = ''
        else:
            l['height'] = str(l['height']) + ' <span class="muted">m</span>'
        string += """\
               <tr>
                  <td class="muted">Height</td>
                  <td>%(height)s</td>
""" % l
        if l['height_wanted_low'] == None and\
           l['height_wanted_high'] == None:
            string+= """\
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
            string += """\
                  <td>%(height_wanted_low)s - %(height_wanted_high)s</td>
""" % l
        string += """\
               </tr>
"""
    return string


def getWeightRowString(l):
    string = ''
    if not(l['weight'] == None and
           l['weight_wanted_low'] == None and
           l['weight_wanted_high'] == None):
        if l['weight'] == None:
            l['weight'] = ''
        else:
            l['weight'] = str(l['weight']) + ' <span class="muted">kg</span>'
        string += """\
               <tr>
                  <td class="muted">Weight</td>
                  <td>%(weight)s</td>
""" % l
        if l['weight_wanted_low'] == None and\
           l['weight_wanted_high'] == None:
            string += """\
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
            string += """\
                  <td>%(weight_wanted_low)s - %(weight_wanted_high)s</td>
"""
        string += """\
               </tr>
"""
    return string


def getEditorRowString(l):
    string = ''
    if not (l['editor'] == None and l['editor_wanted'] == None):
        if l['editor'] == None:
            l['editor'] = ''
        if l['editor_wanted'] == None:
            l['editor_wanted'] = ''
        string += """
                       <tr>
                          <td class="muted">Editor</td>
                          <td>%(editor)s</td>
                          <td>%(editor_wanted)s</td>
                       </tr>
        """ % l
    return string
def getEngineeringDisciplineRowString(l):
    string = ''
    if not (l['engineering_discipline'] == None and l['engineering_discipline_wanted'] == None):
        if l['engineering_discipline'] == None:
            l['engineering_discipline'] = ''
        if l['engineering_discipline_wanted'] == None:
            l['engineering_discipline_wanted'] = ''
        string += """
               <tr>
                  <td class="muted">Engineering Discipline</td>
                  <td>%(engineering_discipline)s</td>
                  <td>%(engineering_discipline_wanted)s</td>
               </tr>
        """ % l
    return string
def getFavoriteStarWarsMovieRowString(l):
    string = ''
    if not (l['favorite_star_wars_movie'] == None and l['favorite_star_wars_movie_wanted'] == None):
        if l['favorite_star_wars_movie'] == None:
            l['favorite_star_wars_movie'] = ''
        if l['favorite_star_wars_movie_wanted'] == None:
            l['favorite_star_wars_movie_wanted'] = ''
        string += """
               <tr>
                  <td class="muted">Favorite Star Wars Film</td>
                  <td>%(favorite_star_wars_movie)s</td>
                  <td>%(favorite_star_wars_movie_wanted)s</td>
               </tr>
        """ % l
    return string


def getGenderRowString(l):
    if not(l['gender'] == None and l['gender_wanted'] == None):
        if l['gender'] == None:
            l['gender'] = ''
        if l['gender_wanted'] == None:
            l['gender_wanted'] = ''
        return """\
               <tr>
                  <td class="muted">Gender </td>
                  <td>%(gender)s</td>
                  <td>%(gender_wanted)s</td>
               </tr>
""" % l
    else:
        return ''


def getProgrammingLanguageRowString(l):
    string = ''
    if not(l['user_programming_languages'] == None and l['user_programming_languages_wanted'] == None):
        lang = ''
        lang_wanted = ''
        if(l['user_programming_languages'] != None):
            for i, langKey in enumerate(l['user_programming_languages']):
                if i != 0:
                    lang += ", "
                lang += langKey['programming_language']
        if(l['user_programming_languages_wanted'] != None):
            for i, langKey in  enumerate(l['user_programming_languages_wanted']):
                if i != 0:
                    lang += ", "
                lang_wanted += langKey['programming_language']
        string += """\
               <tr>
                  <td class="muted">Programming Languages</td>
                  <td>%(lang)s</td>
                  <td>%(lang_wanted)s</td>
               </tr>
""" % {'lang':lang, 'lang_wanted':lang_wanted}
    return string
def getOperatingSystemRowString(l):
    string = ''
    if not(l['user_operating_systems'] == None and l['user_operating_systems_wanted'] == None):
        os = ''
        os_wanted = ''
        if(l['user_operating_systems'] != None):
            for i, langKey in enumerate(l['user_operating_systems']):
                if i != 0:
                    os += ", "
                os += langKey['operating_system']
        if(l['user_operating_systems_wanted'] != None):
            for i, langKey in  enumerate(l['user_operating_systems_wanted']):
                if i != 0:
                    os_wanted += ", "
                os_wanted += langKey['operating_system']
        string += """\
               <tr>
                  <td class="muted">Programming Languages</td>
                  <td>%(os)s</td>
                  <td>%(os_wanted)s</td>
               </tr>
""" % {'os':os, 'os_wanted':os_wanted}
    return string