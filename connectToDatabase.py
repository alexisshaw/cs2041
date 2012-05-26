__author__ = 'ashaw'

import os
import sys

sys.path.append(os.getcwd()+os.sep+'pg'+os.sep+'lib'+os.sep+'python'+os.sep)

import psycopg2

def connect():
    return psycopg2.connect(database = '2041ass2',
        password = 'aYGOVVSmg4MfdZLg9Q5y',
        user = 'cgiclient',
        host = 'ates466.srvr',
        port = 5432)
