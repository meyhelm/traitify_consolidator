import json
import urllib2

#This lambda function uses TERA to search for the candidate's record in elastic search using their candidate id.
#Then, their record is updated with darkData.

def lambda_handler(event, context):

    message = json.loads(event['Records'][0]['Sns']['Message'])
    locatorKey = message['locatorKey']
    candidateId = message['candidateId']
    uClassifyData = message['uClassify']

    lookup = {}
    lookup['resultType'] = 'candidate'
    lookup['searchValue'] = candidateId
    lookup['vectorVersion'] = '2.6'
    lookup['searchType'] = 'id'

    req = urllib2.Request(url='http://tera-traitify.us-west-2.elasticbeanstalk.com/search/')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(lookup))
    esjson = response.read()

    try:
        temp_dict = json.loads(esjson)
        temp_dict['uClassify'] = uClassifyData

    except UnicodeDecodeError as exception:
        temp_dict = json.loads(esjson.decode('utf-8','ignore').encode("utf-8"))
        temp_dict['uClassify'] = uClassifyData

    new_dict = {}
    new_dict['type'] = 'candidate'
    new_dict['id'] = candidateId
    new_dict['candidate'] = temp_dict

    print(candidateId)
    print(new_dict['candidate']['uClassify'])

    index = urllib2.Request(url='http://tera-traitify.us-west-2.elasticbeanstalk.com/index/')
    index.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(index, json.dumps(new_dict))

    print("It went all the way through!")
