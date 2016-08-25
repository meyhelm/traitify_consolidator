import json
import boto3
import uuid

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

#This lambda recieves the Traitify JSON file, as well as its location (bucket and key)
#Then it takes only the results and creates a new (and smaller) JSON file
#Sends the new, smaller JSON to lambda #2

def lambda_handler(event, context):

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

    object_summary = s3_resource.ObjectSummary(bucket,key)
    data = json.loads(object_summary.get()['Body'].read())
    new_json = create_new_json(data)

    new_json['Bucket'] = bucket
    new_json['Key'] = key

    client = boto3.client('sns',region_name='us-west-2')
    response = client.publish(
        TargetArn='arn:aws:sns:us-west-2:559710764015:Traitify_clusters',
        Message=json.dumps({'default': json.dumps(new_json)}),
        MessageStructure='json')


def create_new_json(data):

    new_data = {}
    new_data['Email'] = data['email']
    blend = data['personality']['personality_blend']['name']
    new_data['Blend'] = '/'.join(sorted(blend.split('/')))

    traits = []
    for x in range(0,56):
        traits.append(data['personality']['personality_traits'][x]['personality_trait']['name'])

    new_data['Traits'] = traits

    data_dump = json.dumps(new_data)
    new_json = json.loads(data_dump)

    return new_json
