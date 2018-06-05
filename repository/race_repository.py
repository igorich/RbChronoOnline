import pymysql.cursors
import json
import datetime

from repository.base_repo import *
#from race import Race, RaceEncoder

def log(value):
    file = open('/var/www/html/log/testfile.txt','a')

    file.write('\n\n')
    file.write(str(datetime.datetime.now()))
    file.write('\n')
    file.write(value)

    file.close()

def getAllRaces_json():
    return json.dumps(getAllRaces())#, cls=RaceEncoder)

def getAllRaces():
    with db.cursor() as cur:
        cur.execute("SELECT Id, Name, RaceStartTime FROM Races")
        res = []
        for row in cur.fetchall():
            #obj = {}
            #log(str(row))
            #obj['Id'] = row['Id']
            #obj['Name'] = row['Name']
            #obj['RaceStartTime'] = row['Race']
            res.append(row)
        return res

def getRace(id):
    with db.cursor() as cur:
        cur.execute("SELECT Id, Name, RaceStartTime FROM Races WHERE Id = {0}".format(id))
        row = cur.fetchone()
        obj = {}
        obj['Id'] = row[0]
        obj['Name'] = row[1]
        obj['RaceStartTime'] = row[2]
        return obj

def createRace(name, desc, startdate):
    newId = -1
    with db.cursor() as cur:
        cur.execute('INSERT INTO Races (Name, Description, RaceStartTime) VALUES(\'{0}\', \'{1}\', \'{2}\'); SELECT LAST_INSERT_ID();'.format(name, desc, startdate))
        newId = cursor.fetchone()
    db.commit()
    return newId
