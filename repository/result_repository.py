import pymysql.cursors
import json

#import base_repo

def resultsList(raceId):
    with db.cursor() as cur:
        cur.execure('SELECT * FROM Results WHERE RaceIs = {0}'.format(raceId))

#def createResult(raceId, compId, result):
    #
