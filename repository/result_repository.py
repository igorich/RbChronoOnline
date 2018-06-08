import pymysql.cursors
import json

from repository.race_repository import *

#import base_repo
class ResultRepository:
    #def __init__(self):
    def resultsList(raceId):
        with db.cursor() as cur:
            cur.execute('SELECT r.Id, r.CompetitorId, r.RaceId, r.ResultText, r.ResultTime, '
                        + ' c.StartNumber, c.Name, c.CarModel, c.ClassText '
                        + 'FROM Results as r '
                        + 'LEFT JOIN Competitors as c ON r.CompetitorId = c.Id '
                        + 'WHERE RaceId = {0}'
                .format(raceId))
            res = []
            for row in cur.fetchall():
                res.append(row)
            return res		

    #def createResult(raceId, compId, result):
        #