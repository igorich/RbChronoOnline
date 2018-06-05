import json

class Race:
	raceId = 0
	name = ""
	RaceStartTime = ""

class RaceEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Race):
            return { "raceId" : obj.raceId, "name": obj.name, "RaceStartTime": obj.RaceStartTime }
        return json.JSONEncoder.default(self, obj)