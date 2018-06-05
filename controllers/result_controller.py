# from swagger_server.models.api_response import ApiResponse  # noqa: E501
# from swagger_server.models.pet import Pet  # noqa: E501
# from swagger_server import util

import repository.result_repository

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
    id = result_repository.createResult(
        req_data.get('RaceId')
        , 1
        ,req_data.get('Result')        
    )
    return 'add new result with id ' + id
