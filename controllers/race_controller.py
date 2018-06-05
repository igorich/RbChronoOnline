
import repository.race_repository
import json
from flask import Flask, render_template, request, make_response, jsonify
#from repository/race import repo_getAllRaces, repo_getAllRaces_json

# from swagger_server.models.api_response import ApiResponse  # noqa: E501
# from swagger_server.models.pet import Pet  # noqa: E501
# from swagger_server import util

@app.route('/race/', methods=['GET'])
def getAllRace():

    result = race_repository.getAllRaces_json()

    resp = make_response(result.replace("\'", "\""))
    resp.headers['Content-Type'] = 'application/json'
    resp.mimetype = 'application/json'
    return resp

@app.route('/race/<int:race_id>', methods=['GET'])
def getRace(race_id):
    content = race_repository.getRace(race_id)
    return jsonify(content)

@app.route('/race/', methods=['POST'])
def addRace(race_id):
    req_data = request.get_json()
    newId = race_repository.createRace(
        req_data.get('name')
        ,req_data.get('description')
        ,req_data.get('startdate')
    )
    return 'add new race with id ' + newId

