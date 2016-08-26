import urllib2
import json as J
import ssl
import boto3
import os
import uClassify_utils as u


host = 'https://api.uclassify.com/v1/'
end_points = ['prfekt/mood/classify','prfekt/tonality/classify', 'prfekt/direction-aqal-jung/classify', 'prfekt/values/classify', 'uclassify/iab-taxonomy/classify']
key = 'Token PUTTOKENHERE'


#This lambda function will take a person's xml file then extract their candidate id and locator key.
#Then, using the locator key, TERA finds the candidate's record and extracts their resume description.
#After that, the resume description is run through the uClassify service.
#The uClassify results are saved as a json file in the candidate's s3 metro bucket.
#Top terms/values aka "darkData" are extracted from the uClassify results.
#The candidate id, locator key, and darkData are sent as the message of an SNS to Lambda #2

def lambda_handler(event, context):

    message = event['Records'][0]['Sns']['Message']     #this is used for testing purposes
    #message = J.loads(event['Records'][0]['Sns']['Message'])
    locatorKey = message['LocatorKey']
    candidateId = message['CandidateId']
    bucket = message['MetroBucketName']
    folder = message['MetroKey']

    lookup = {}
    lookup['inputType'] = 'locatorKey'
    lookup['resultData'] = ['resumeText']
    lookup['inputValue'] = locatorKey

    #call TERA
    req = urllib2.Request(url='http://es-rest-services-tortuga.us-west-2.elasticbeanstalk.com/parse')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, J.dumps(lookup))

    #extract resumeText
    tera_json = J.loads(response.read())
    resume_text = tera_json['resumeText']

    #run text through uClassify service
    classified = u.process_text(resume_text)
    u.insert_metro_s3(bucket, folder, 'uClassify.json', J.dumps(classified))
    print("Text processed!")

    #extract uClassify values and put into new dict
    darkData = {}
    darkData['values'] = u.top_values(classified)
    darkData['taxonomy'] = u.top_taxonomy(classified)
    darkData['focus'] = u.top_focus(classified)
    darkData['tone'] = u.top_tone(classified)
    darkData['mood'] = u.top_mood(classified)

    #create SNS message to send to next lambda to update ES
    new_message = {}
    new_message['candidateId'] = candidateId
    new_message['locatorKey'] = locatorKey
    new_message['uClassify'] = darkData

    client = boto3.client('sns',region_name='us-west-2')
    response = client.publish(
        TargetArn='arn:aws:sns:us-west-2:559710764015:darkData',
        Message=J.dumps({'default': J.dumps(new_message)}),
        MessageStructure='json')

    print("Everything Works!")
