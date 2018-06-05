from flask import Flask, render_template, request, make_response, jsonify
from flask_swagger import swagger
import json
import datetime

#import repository.result_repository
from repository.race_repository import *

#export FLASK_DEBUG=1
app = Flask(__name__)

@app.route('/')
def index():
    r = getAllRaces()
    return render_template('index2.html', races=r)

@app.route('/spec')
def spec():
    swag = swagger(app)
    swag['info']['version'] = '1.0'
    swag['info']['title'] = 'RbChrono API'
    return jsonify(swag)

@app.route('/up')
def hello():
	return 'Hello, World'

def log(value):
    file = open('/var/www/html/log/testfile.txt','a')
 
    file.write('\n\n')
    file.write(str(datetime.datetime.now()))
    file.write('\n')
    file.write(value)
 
    file.close()

'''
race_controller
'''
@app.route('/race/', methods=['GET'])
def getAllRace():

    result = getAllRaces_json()

    resp = make_response(result.replace('\'', '\''))
    resp.headers['Content-Type'] = 'application/json'
    resp.mimetype = 'application/json'
    return resp

@app.route('/race/<int:race_id>', methods=['GET'])
def getRace(race_id):
    content = race_repository.getRace(race_id)
    return jsonify(content)

@app.route('/race/', methods=['POST'])
def addRace():
    req_data = request.get_json()
    newId = createRace(
        req_data.get('name')
        ,req_data.get('description')
        ,req_data.get('startdate')
    )
    return 'add new race with id ' + newId

'''
result_controller
'''
@app.route('/race/<int:raceId>/results/', methods=['GET'])
def raceResults(raceId):
    list1 = result_repository.resultsList(raceId)
    return list1

@app.route('/result/<int:resultId>', methods=['GET'])
def getResult(resultId):
    return 'return result with id ' + resultId

@app.route('/result/', methods=['POST'])
def addResult():
    req_data = request.get_json()
    id = createResult(
        req_data.get('RaceId')
        , 1
        ,req_data.get('Result')        
    )
    return 'add new result with id ' + id
