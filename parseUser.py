import os
import re
import sys

sys.path.append(os.getcwd()+os.sep+'pg'+os.sep+'lib'+os.sep+'python'+os.sep)

import psycopg2

__author__ = 'WS02admin'

def parseUser(connection, dir):
    username = None
    password = None
    name = None
    dob = None
    email = None
    age_wanted_high = None
    age_wanted_low = None
    gender = None
    gender_wanted = None
    height = None
    height_wanted_low = None
    height_wanted_high = None
    weight = None
    weight_wanted_high = None
    weight_wanted_low = None
    engineering_discipline = None
    engineering_discipline_wanted = None
    favorite_star_wars_movie = None
    favorite_star_wars_movie_wanted = None
    operating_systems = None
    operating_systems_wanted = None
    programming_languages = None
    programming_languages_wanted = None
    editor = None
    editor_wanted = None
    image = None
    if os.path.isfile(dir + os.sep + 'profile'):
        userProfile = open(dir + os.sep + 'profile', 'r', )
        switch = None
        for line in userProfile.readlines():
            if re.match("^username", line):
                m = re.match(r"^username:                (.*)\n", line)
                username = m.group(1)
            elif re.match("^password", line):
                m = re.match(r"^password:                (.*)\n", line)
                password = m.group(1)
            elif re.match("^name", line):
                m = re.match(r"^name:                    (.*)\n", line)
                name = m.group(1)
            elif re.match("^DOB", line):
                m = re.match(r"^DOB:                     (.*)\n", line)
                dob = m.group(1)
            elif re.match("^email", line):
                m = re.match(r"^email:                   (.*)\n", line)
                email = m.group(1)

            elif re.match("^age", line):
                switch = 'age'
            elif re.match("^    looking_for:", line) and switch == 'age':
                m = re.search(r"min: (\d+), max: (\d+)", line)
                age_wanted_low = m.group(1)
                age_wanted_high = m.group(2)

            elif re.match("^gender", line):
                switch = 'gender'
            elif re.match("^    looking_for:", line) and switch == 'gender':
                m = re.search(r": *([MmFf])", line)
                gender_wanted = m.group(1).upper() if m != None else None
            elif re.match("^    me:", line) and switch == 'gender':
                m = re.search(r": *([MmFf])", line)
                gender = m.group(1).upper() if m != None else None

            elif re.match("^height", line):
                switch = 'height'
            elif re.match("^    looking_for", line) and switch == 'height':
                m = re.search("min: ([0-9.]+), max: ([0-9.]+)", line)
                height_wanted_low = m.group(1)
                height_wanted_high = m.group(2)
            elif re.match("^    me", line) and switch == 'height':
                m = re.search('([0-9.]+)', line)
                height = m.group(1)

            elif re.match("^weight", line):
                switch = 'weight'
            elif re.match("^    looking_for:", line) and switch == 'weight':
                m = re.search(r"min: (\d+), max: (\d+)", line)
                weight_wanted_low = m.group(1)
                weight_wanted_high = m.group(2)
            elif re.match("^    me", line) and switch == 'weight':
                m = re.search('(\d+)', line)
                weight = m.group(1)
            elif re.match("^engineering_discipline", line):
                switch = 'eng'
            elif re.match("^    looking_for", line) and switch == 'eng':
                m = re.search(r': *(\w+)', line)
                engineering_discipline_wanted = m.group(1)
            elif re.match("^    me", line) and switch == 'eng':
                m = re.search(r': *(\w+)', line)
                engineering_discipline = m.group(1)

            elif re.match("^favourite_star_wars_movie", line):
                switch = 'star_wars'
            elif re.match("^    looking_for", line) and switch == 'star_wars':
                m = re.search(r': *([^\n]+)', line)
                favorite_star_wars_movie_wanted = m.group(1)
            elif re.match("^    me", line) and switch == 'star_wars':
                m = re.search(r': *([^\n]+)', line)
                favorite_star_wars_movie = m.group(1)

            elif re.match("^operating_systems", line):
                switch = 'os'
            elif re.match("^    looking_for", line) and switch == 'os':
                m = re.search("\{([^}]+)\}", line)
                operating_systems_wanted_string = m.group(1)
                operating_systems_wanted = operating_systems_wanted_string.split(',')
            elif re.match("^    me", line) and switch == 'os':
                m = re.search("\{([^}]+)\}", line)
                operating_systems_string = m.group(1)
                operating_systems = operating_systems_string.split(',')

            elif re.match("^programming_languages", line):
                switch = 'lang'
            elif re.match("^    looking_for", line) and switch == 'lang':
                m = re.search("\{([^}]+)\}", line)
                programming_languages_wanted_string = m.group(1)
                programming_languages_wanted = programming_languages_wanted_string.split(',')
            elif re.match("^    me", line) and switch == 'lang':
                m = re.search("\{([^}]+)\}", line)
                programming_languages_string = m.group(1)
                programming_languages = programming_languages_string.split(',')

            elif re.match("^editor", line):
                switch = 'editor'
            elif re.match("^    looking_for", line) and switch == 'editor':
                m = re.search(": *([^\n]+)", line)
                editor_wanted = m.group(1)
            elif re.match("^    me", line) and switch == 'editor':
                m = re.search(": *([^\n]+)", line)
                editor = m.group(1)

    if os.path.isfile(dir + os.sep + 'image.jpg'):
        image= open(dir + os.sep + 'image.jpg')


    c = connection.cursor()
    if operating_systems is not None:
        for operatingSystem in operating_systems:
            osTemp = operatingSystem.strip()
            c.execute("SELECT operating_system FROM operating_systems WHERE operating_system = %s", [osTemp])
            if c.fetchone() is None:
                c.execute("INSERT INTO operating_systems values (%s)", [osTemp])
    if operating_systems_wanted is not None:
        for operatingSystem in operating_systems_wanted:
            osTemp = operatingSystem.strip()
            c.execute("SELECT operating_system FROM operating_systems WHERE operating_system = %s",[osTemp])
            if c.fetchone() is None:
                c.execute("INSERT INTO operating_systems values (%s)", [osTemp])
    if programming_languages is not None:
        for pl in programming_languages:
            plTemp = pl.strip()
            c.execute("SELECT programming_language FROM programming_languages WHERE programming_language = %s",[plTemp])
            if c.fetchone() is None:
                c.execute("INSERT INTO programming_languages values (%s)", [plTemp])
    if programming_languages_wanted is not None:
        for pl in programming_languages_wanted:
            plTemp = pl.strip()
            c.execute("SELECT programming_language FROM programming_languages WHERE programming_language = %s", [plTemp])
            if c.fetchone() is None:
                c.execute("INSERT INTO programming_languages values (%s)", [plTemp])
    if favorite_star_wars_movie is not None:
        c.execute("SELECT movie_name FROM star_wars_movies WHERE movie_name = %s", [favorite_star_wars_movie.strip()])
        if c.fetchone() is None:
            c.execute("INSERT INTO star_wars_movies values(%s)", [favorite_star_wars_movie.strip()])
    if favorite_star_wars_movie_wanted is not None:
        c.execute("SELECT movie_name FROM star_wars_movies WHERE movie_name = %s", [favorite_star_wars_movie_wanted.strip()])
        if c.fetchone() is None:
            c.execute("INSERT INTO star_wars_movies values(%s)", [favorite_star_wars_movie_wanted.strip()])
    if editor is not None:
        c.execute("SELECT editor FROM editors WHERE editor = %s", [editor.strip()])
        if c.fetchone() is None:
            c.execute("INSERT INTO editors values(%s)", [editor.strip()])
    if editor_wanted is not None:
        c.execute("SELECT editor FROM editors WHERE editor = %s", [editor_wanted.strip()])
        if c.fetchone() is None:
            c.execute("INSERT INTO editors values(%s)", [editor_wanted.strip()])
    if engineering_discipline is not None:
         c.execute("SELECT engineering_discipline FROM engineering_disciplines WHERE engineering_discipline = %s",
                    [engineering_discipline.strip()])
         if c.fetchone() is None:
            c.execute("INSERT INTO engineering_disciplines values(%s)", [engineering_discipline.strip()])
    if engineering_discipline_wanted is not None:
         c.execute("SELECT engineering_discipline FROM engineering_disciplines WHERE engineering_discipline = %s",
                    [engineering_discipline_wanted.strip()])
         if c.fetchone() is None:
            c.execute("INSERT INTO engineering_disciplines values(%s)", [engineering_discipline_wanted.strip()]) 
    c.execute("INSERT INTO users values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,, 'Active' CURRENT_TIMESTAMP - INTERVAL 1 DAY , "")",
        [username,
         password.decode("utf-8"),
         name,
         convertDOB(dob),
         email,
         age_wanted_high,
         age_wanted_low,
         gender,
         gender_wanted,
         height,
         height_wanted_high,
         height_wanted_low,
         weight,
         weight_wanted_high,
         weight_wanted_low,
         engineering_discipline,
         engineering_discipline_wanted,
         editor,
         editor_wanted,
         favorite_star_wars_movie,
         favorite_star_wars_movie_wanted,
         psycopg2.Binary(image.read()) if image is not None else None ])
    if operating_systems is not None:
        for operatingSystem in operating_systems:
            c.execute("INSERT INTO user_operating_systems values (DEFAULT,%s,%s)", [username,operatingSystem.strip()])
    if operating_systems_wanted is not None:
        for operatingSystem in operating_systems_wanted:
            c.execute("INSERT INTO user_operating_system_wanted values (DEFAULT,%s,%s)", [username,operatingSystem.strip()])
    if programming_languages is not None:
        for pl in programming_languages:
            c.execute("INSERT INTO user_programming_languages  values (DEFAULT,%s,%s)", [username,pl.strip()])
    if programming_languages_wanted is not None:
        for pl in programming_languages_wanted:
            c.execute("INSERT INTO user_programming_languages_wanted values (DEFAULT,%s,%s)", [username,pl.strip()])
    connection.commit()
    print username
    c.close()

def convertDOB(dob):
    m = re.search(r"(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})", dob)
    return psycopg2.Date(int(m.group('year')), int(m.group('month')), int(m.group('day')))