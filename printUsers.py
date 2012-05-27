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