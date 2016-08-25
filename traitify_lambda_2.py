import json
import urllib2
import boto3

#This lambda recieves the small json as a message.
#Then is uses the candidate's email to search w/ TERA for their record
#Then it updates the candidate's record with the Traitify results
#A message is sent to the next lambda (#3) that has the bucket and key location of the original Traitify JSON,
# as well as the candidate id

def lambda_handler(event, context):

    message = json.loads(event['Records'][0]['Sns']['Message'])
    email = message['Email']

    lookup = {}
    lookup['resultType'] = 'candidate'
    lookup['searchValue'] = email
    lookup['vectorVersion'] = '2.6'
    lookup['searchType'] = 'email'

    req = urllib2.Request(url='http://tera-traitify.us-west-2.elasticbeanstalk.com/search/')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(lookup))

    traits = message['Traits'][0:5]

    esjson = response.read()

    try:
        temp_dict = json.loads(esjson)
        temp_dict['traitifyClusters'] = traits

    except UnicodeDecodeError as exception:
        temp_dict = json.loads(esjson.decode('utf-8','ignore').encode("utf-8"))
        temp_dict['traitifyClusters'] = traits

    new_dict = {}
    new_dict['type'] = 'candidate'
    new_dict['id'] = temp_dict['candidateId']
    new_dict['candidate'] = temp_dict

    index = urllib2.Request(url='http://tera-traitify.us-west-2.elasticbeanstalk.com/index/')
    index.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(index, json.dumps(new_dict))

    new_message = {}
    new_message['id'] = new_dict['id']
    new_message['Bucket'] = message['Bucket']
    new_message['Key'] = message['Key']

    client = boto3.client('sns',region_name='us-west-2')
    response = client.publish(
        TargetArn='arn:aws:sns:us-west-2:559710764015:update_traitify_dynamo',
        Message=json.dumps({'default': json.dumps(new_message)}),
        MessageStructure='json')
