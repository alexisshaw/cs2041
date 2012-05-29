__author__ = 'WS02admin'

def dropTables(connection):
    connection.execute("DROP TABLE IF EXISTS user_operating_systems")
    connection.execute("DROP TABLE IF EXISTS user_operating_system_wanted")
    connection.execute("DROP TABLE IF EXISTS operating_systems")
    connection.execute("DROP TABLE IF EXISTS user_programming_languages")
    connection.execute("DROP TABLE IF EXISTS user_programming_languages_wanted")
    connection.execute("DROP TABLE IF EXISTS programming_languages")
    connection.execute("DROP TABLE IF EXISTS loginData")
    connection.execute("DROP TABLE IF EXISTS users")
    connection.execute("DROP TABLE IF EXISTS editors")
    connection.execute("DROP TABLE IF EXISTS star_wars_movies")
    connection.execute("DROP TABLE IF EXISTS engineering_disciplines")
    connection.execute("DROP TYPE IF EXISTS gender_type")

def createTables(connection):
    connection.execute("""\
CREATE TABLE star_wars_movies (
    movie_name    VARCHAR(60) PRIMARY KEY NOT NULL UNIQUE
)""")
    connection.execute("""\
CREATE TABLE engineering_disciplines (
    engineering_discipline     VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
);""")
    connection.execute("""\
CREATE TABLE editors (
    editor    VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
);""")
    connection.execute("CREATE TYPE gender_type AS ENUM ('M','F')")
    connection.execute("""\
CREATE TABLE users (
   userid                          VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE,
   pass                            VARCHAR(255) NOT NULL,
   name                            VARCHAR(255) NOT NULL,
   dob                             DATE NOT NULL, 
   email                           VARCHAR(255) NOT NULL,
   age_wanted_high                 INT,
   age_wanted_low                  INT,
   gender                          gender_type,
   gender_wanted                   gender_type,
   height                          NUMERIC,
   height_wanted_high              NUMERIC,
   height_wanted_low               NUMERIC,
   weight                          INT,
   weight_wanted_high              INT,
   weight_wanted_low               INT,
   engineering_discipline          VARCHAR(255)  REFERENCES engineering_disciplines(engineering_discipline),
   engineering_discipline_wanted   VARCHAR(255)  REFERENCES engineering_disciplines(engineering_discipline),
   editor                          VARCHAR(255) REFERENCES editors(editor),
   editor_wanted                   VARCHAR(255) REFERENCES editors(editor),
   favorite_star_wars_movie        VARCHAR(60) REFERENCES star_wars_movies(movie_name),
   favorite_star_wars_movie_wanted VARCHAR(60) REFERENCES star_wars_movies(movie_name),
   image                           bytea,
   --Checks
   CHECK (dob < current_date),
   CHECK (age_wanted_low = NULL or age_wanted_low > 0),
   CHECK (age_wanted_low = NULL or age_wanted_low  < age_wanted_high),
   CHECK (height_wanted_low = NULL or height_wanted_low > 0),
   CHECK (height_wanted_low = NULL or height_wanted_low  < height_wanted_high),
   CHECK (weight_wanted_low = NULL or weight_wanted_low > 0),
   CHECK (weight_wanted_low = NULL or weight_wanted_low  < height_wanted_high)
   );""")
    connection.execute("""\
CREATE TABLE logindata(
    login_token  CHAR(32) PRIMARY KEY NOT NULL UNIQUE,
    userid       VARCHAR(255) NOT NULL REFERENCES users(userid) ON DELETE CASCADE,
    lastUsed     timestamp with time zone NOT NULL,
    autoLogout   boolean   NOT NULL
)""")

    connection.execute("""\
CREATE TABLE operating_systems (
   operating_system         VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
   )""")
    connection.execute("""\
CREATE TABLE user_operating_systems (
   row_no                   SERIAL PRIMARY KEY,
   userid                   VARCHAR(255) NOT NULL REFERENCES users(userid) ON DELETE CASCADE,
   operating_system         VARCHAR(255) NOT NULL REFERENCES operating_systems(operating_system) ON DELETE CASCADE
   )""")
    connection.execute("""\
CREATE TABLE user_operating_system_wanted (
   row_no                   SERIAL PRIMARY KEY,
   userid                   VARCHAR(255) NOT NULL REFERENCES users(userid) ON DELETE CASCADE,
   operating_system         VARCHAR(255) NOT NULL REFERENCES operating_systems(operating_system) ON DELETE CASCADE
   )""")
    connection.execute("""\
CREATE TABLE programming_languages (
    programming_language    VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
)""")
    connection.execute("""\
CREATE TABLE user_programming_languages (
   row_no                   SERIAL PRIMARY KEY,
   userid                   VARCHAR(255) NOT NULL REFERENCES users(userid) ON DELETE CASCADE,
   programming_language     VARCHAR(255) NOT NULL REFERENCES programming_languages(programming_language) ON DELETE CASCADE
   )""")
    connection.execute("""\
CREATE TABLE user_programming_languages_wanted (
   row_no                   SERIAL PRIMARY KEY,
   userid                   VARCHAR(255) NOT NULL REFERENCES users(userid) ON DELETE CASCADE,
   programming_language     VARCHAR(255) NOT NULL REFERENCES programming_languages(programming_language) ON DELETE CASCADE
   )""")
