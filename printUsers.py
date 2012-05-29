import connectToDatabase
from printUser import getUserBioSummaryString

__author__ = 'ashaw'

def fetchAdditionalProfileInfo(l, internalCursor):
    internalCursor.execute("SELECT operating_system FROM user_operating_systems " +
                           "WHERE user_operating_systems.userid = %s " +
                           "ORDER BY operating_system ASC", [l['userid']])
    l['user_operating_systems'] = internalCursor.fetchall()
    internalCursor.execute("SELECT operating_system FROM user_operating_system_wanted " +
                           "WHERE user_operating_system_wanted.userid = %s " +
                           "ORDER BY operating_system ASC", [l['userid']])
    l['user_operating_systems_wanted'] = internalCursor.fetchall()
    internalCursor.execute("SELECT programming_language FROM user_programming_languages " +
                           "WHERE user_programming_languages.userid = %s " +
                           "ORDER BY programming_language ASC", [l['userid']])
    l['user_programming_languages'] = internalCursor.fetchall()
    internalCursor.execute("SELECT programming_language FROM user_programming_languages_wanted " +
                           "WHERE user_programming_languages_wanted.userid = %s " +
                           "ORDER BY programming_language ASC", [l['userid']])
    l['user_programming_languages_wanted'] = internalCursor.fetchall()
    return l


def printUserProfilesInternal(query, values):
    string = ''
    conn = connectToDatabase.connect(dictCon=True)
    users = conn.cursor()
    internalCursor = conn.cursor()
    users.execute(query, values)
    for user in users:
        l = user
        l = fetchAdditionalProfileInfo(l, internalCursor)
        string += getUserBioSummaryString(l)
    internalCursor.close()
    users.close()
    conn.close()
    return string

def escape(search):
    return search.replace('`','``').replace('_','`_').replace('%','`%')

def getUserProfiles(search, prefix,postfix, limit,page):
    return printUserProfilesInternal("SELECT * FROM USERS WHERE userid ILIKE and account_status = 'Active' %s ESCAPE '`' ORDER BY userid ASC LIMIT %s OFFSET %s", [prefix + escape(search) + postfix, limit, page*limit ])

def countUserProfiles(search, prefix,postfix):
    conn  = connectToDatabase.connect()
    count = conn.cursor()
    count.execute("SELECT count(*) FROM USERS WHERE userid and account_status = 'Active' ILIKE %s ESCAPE '`'", [prefix + escape(search) + postfix])
    countValue = count.fetchone()[0]
    count.close()
    conn.close()
    return countValue

def getCount(query,values):
    string = ''
    conn = connectToDatabase.connect(dictCon=True)
    users = conn.cursor()
    internalCursor = conn.cursor()
    users.execute(query, values)
    for user in users:
        l = user
        l = fetchAdditionalProfileInfo(l, internalCursor)
        string += getUserBioSummaryString(l)
    internalCursor.close()
    users.close()
    conn.close()
    return string
