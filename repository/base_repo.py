import pymysql.cursors
import json
#from race import Race, RaceEncoder

db = pymysql.connect(host="localhost",# your host, usually localhost
                     user="dbuser",       # your username
                     password="stopdb",    # your password
                     db="RbChrono",        # name of the data base
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)



def foo():
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM races")

    # print all the first cell of all the rows
    #for row in cur.fetchall():
    #    print row[0]

    #print "finish"

    db.close()
