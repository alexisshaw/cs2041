__author__ = 'ashaw'

import os
import sys

sys.path.append(os.getcwd()+os.sep+'pg'+os.sep+'lib'+os.sep+'python'+os.sep)

import psycopg2
import psycopg2.extras

def connect(dictCon = False):
        return psycopg2.connect(database = '2041ass2',
            password = 'aYGOVVSmg4MfdZLg9Q5y',
            user = 'cgiclient',
            host = 'ates466.srvr',
            port = 5432,
            connection_factory = psycopg2.extras.RealDictConnection if dictCon else psycopg2.extensions.connection )
def getDirBase ():
    return '/~ates466/cs2041/engcupid/'

