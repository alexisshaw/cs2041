import os
import re
import sqlite3

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
                if re.match(r"Male", line):
                    gender_wanted = "M"
                else:
                    gender_wanted = "F"
            elif re.match("^    me:", line) and switch == 'gender':
                if re.search(r"Male", line):
                    gender = "M"
                else:
                    gender = "F"

            elif re.match("^height", line):
                switch = 'height'
            elif re.match("^    looking_for", line) and switch == 'height':
                m = re.search("min: ((?:\d|.)+), max: ((?:\d|.)+)", line)
                height_wanted_low = m.group(1)
                height_wanted_high = m.group(2)
            elif re.match("^    me", line) and switch == 'height':
                m = re.match('((?:\d|.)+)', line)
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
                engineering_discipline = m.group(1)
            elif re.match("^    me", line) and switch == 'eng':
                m = re.search(r': *(\w+)', line)
                engineering_discipline_wanted = m.group(1)

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
            c.execute("SELECT operating_system FROM operating_systems WHERE operating_system = ?", [osTemp])
            if c.fetchone() is None:
                c.execute("INSERT INTO operating_systems values (?)", [osTemp])
    if operating_systems_wanted is not None:
        for operatingSystem in operating_systems_wanted:
            osTemp = operatingSystem.strip()
            c.execute("SELECT operating_system FROM operating_systems WHERE operating_system = ?",[osTemp])
            if c.fetchone() is None:
                c.execute("INSERT INTO operating_systems values (?)", [osTemp])
    if programming_languages is not None:
        for pl in programming_languages:
            plTemp = pl.strip()
            c.execute("SELECT programming_language FROM programming_languages WHERE programming_language = ?",[plTemp])
            if c.fetchone() is None:
                c.execute("INSERT INTO programming_languages values (?)", [plTemp])
    if programming_languages_wanted is not None:
        for pl in programming_languages_wanted:
            plTemp = pl.strip()
            c.execute("SELECT programming_language FROM programming_languages WHERE programming_language = ?", [plTemp])
            if c.fetchone() is None:
                c.execute("INSERT INTO programming_languages values (?)", [plTemp])
    if favorite_star_wars_movie is not None:
        c.execute("SELECT movie_name FROM star_wars_movies WHERE movie_name = ?", [favorite_star_wars_movie])
        if c.fetchone() is None:
            c.execute("INSERT INTO star_wars_movies values(?)", [favorite_star_wars_movie])
    if favorite_star_wars_movie_wanted is not None:
        c.execute("SELECT movie_name FROM star_wars_movies WHERE movie_name = ?", [favorite_star_wars_movie_wanted])
        if c.fetchone() is None:
            c.execute("INSERT INTO star_wars_movies values(?)", [favorite_star_wars_movie_wanted])
    if editor is not None:
        c.execute("SELECT editor FROM editors WHERE editor = ?", [editor])
        if c.fetchone() is None:
            c.execute("INSERT INTO editors values(?)", [editor])
    if editor_wanted is not None:
        c.execute("SELECT editor FROM editors WHERE editor = ?", [editor_wanted])
        if c.fetchone() is None:
            c.execute("INSERT INTO editors values(?)", [editor_wanted])

    c.execute("INSERT INTO users values (?,?,?,julianday(?),?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
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
         sqlite3.Binary(image.read()) if image is not None else None ])
    if operating_systems is not None:
        for operatingSystem in operating_systems:
            c.execute("INSERT INTO user_operating_systems values (?,?,?)", [None,username,operatingSystem.strip()])
    if operating_systems_wanted is not None:
        for operatingSystem in operating_systems_wanted:
            c.execute("INSERT INTO user_operating_system_wanted values (?,?,?)", [None,username,operatingSystem.strip()])
    if programming_languages is not None:
        for pl in programming_languages:
            c.execute("INSERT INTO user_programming_languages  values (?,?,?)", [None,username,pl.strip()])
    if programming_languages_wanted is not None:
        for pl in programming_languages_wanted:
            c.execute("INSERT INTO user_programming_languages_wanted values (?,?,?)", [None,username,pl.strip()])
    connection.commit()

def convertDOB(dob):
    m = re.search(r"(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})", dob)
    return '' + m.group('year') + '-' + m.group('month') + '-' + m.group('day')