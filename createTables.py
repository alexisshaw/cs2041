__author__ = 'WS02admin'

def dropTables(connection):
    connection.execute("DROP TABLE IF EXISTS user_operating_systems")
    connection.execute("DROP TABLE IF EXISTS user_operating_system_wanted")
    connection.execute("DROP TABLE IF EXISTS operating_systems")
    connection.execute("DROP TABLE IF EXISTS user_programming_languages")
    connection.execute("DROP TABLE IF EXISTS user_programming_languages_wanted")
    connection.execute("DROP TABLE IF EXISTS programming_languages")
    connection.execute("DROP TABLE IF EXISTS users")
    connection.execute("DROP TABLE IF EXISTS editors")
    connection.execute("DROP TABLE IF EXISTS star_wars_movies")
    connection.execute("DROP TABLE IF EXISTS engineering_disciplines")


def createTables(connection):
    connection.execute("""\
CREATE TABLE IF NOT EXISTS star_wars_movies (
    movie_name    CHAR(60) PRIMARY KEY NOT NULL UNIQUE
)""")
    connection.execute("""\
CREATE TABLE IF NOT EXISTS engineering_disciplines (
    engineering_discipline     CHAR(60) PRIMARY KEY NOT NULL UNIQUE
)""")
    connection.execute("""\
CREATE TABLE IF NOT EXISTS editors (
    editor    VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
)""")
    connection.execute("""\
CREATE TABLE IF NOT EXISTS users (
   user                            VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE,
   pass                            VARCHAR(255) NOT NULL,
   name                            VARCHAR(255) NOT NULL,
   dob                             REAL NOT NULL, -- Sqlite does not support date
   email                           VARCHAR(255) NOT NULL,
   age_wanted_high                 INT(4),
   age_wanted_low                  INT(4),
   gender                          CHAR(1),
   gender_wanted                   CHAR(1),
   height                          REAL,
   height_wanted_high              REAL,
   height_wanted_low               REAL,
   weight                          INT(3),
   weight_wanted_high              INT(3),
   weight_wanted_low               INT(3),
   engineering_discipline          VARCHAR(255)  REFERENCES engineering_disciplines(engineering_discipline),
   engineering_discipline_wanted   VARCHAR(255)  REFERENCES engineering_disciplines(engineering_discipline),
   editor                          VARCHAR(255) REFERENCES editors(editor),
   editor_wanted                   VARCHAR(255) REFERENCES editors(editor),
   favorite_star_wars_movie        CHAR(60) REFERENCES star_wars_movies(movie_name),
   favorite_star_wars_movie_wanted CHAR(60) REFERENCES star_wars_movies(movie_name),
   image                           BLOB,
   --Checks
   CHECK (gender IN ("M","F", NULL)),
   CHECK (gender_wanted IN ("M","F", NULL)),
   CHECK (dob < julianday('now')),
   CHECK (age_wanted_low == NULL or age_wanted_low > 0),
   CHECK (age_wanted_low == NULL or age_wanted_low  < age_wanted_high),
   CHECK (height_wanted_low == NULL or height_wanted_low > 0),
   CHECK (height_wanted_low == NULL or height_wanted_low  < height_wanted_high),
   CHECK (weight_wanted_low == NULL or weight_wanted_low > 0),
   CHECK (weight_wanted_low == NULL or weight_wanted_low  < height_wanted_high)
   )""")
    connection.execute("""\
CREATE TABLE IF NOT EXISTS operating_systems (
   operating_system         VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
   )""")
    connection.execute("""\
CREATE TABLE IF NOT EXISTS user_operating_systems (
   row_no                   INTEGER PRIMARY KEY,
   user                     VARCHAR(255) NOT NULL REFERENCES users(user) ON DELETE CASCADE,
   operating_system         VARCHAR(255) NOT NULL REFERENCES operating_systems(operating_system) ON DELETE CASCADE
   )""")
    connection.execute("""\
CREATE TABLE IF NOT EXISTS user_operating_system_wanted (
   row_no                   INTEGER PRIMARY KEY,
   user                     VARCHAR(255) NOT NULL REFERENCES users(user) ON DELETE CASCADE,
   operating_system         VARCHAR(255) NOT NULL REFERENCES operating_systems(operating_system) ON DELETE CASCADE
   )""")
    connection.execute("""\
CREATE TABLE IF NOT EXISTS programming_languages (
    programming_language    VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
)""")
    connection.execute("""\
CREATE TABLE IF NOT EXISTS user_programming_languages (
   row_no                   INTEGER PRIMARY KEY,
   user                     VARCHAR(255) NOT NULL REFERENCES users(user) ON DELETE CASCADE,
   programming_language     VARCHAR(255) NOT NULL REFERENCES programming_languages(programming_language) ON DELETE CASCADE
   )""")
    connection.execute("""\
CREATE TABLE IF NOT EXISTS user_programming_languages_wanted (
   row_no                   INTEGER PRIMARY KEY,
   user                     VARCHAR(255) NOT NULL REFERENCES users(user) ON DELETE CASCADE,
   programming_language     VARCHAR(255) NOT NULL REFERENCES programming_languages(programming_language) ON DELETE CASCADE
   )""")