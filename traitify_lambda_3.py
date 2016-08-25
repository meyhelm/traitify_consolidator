import json
import boto3

#This lambda looks up the candidate in the DynamoDB table and puts the bucket & key of the location of
# the original Traitify JSON in the table

def lambda_handler(event, context):

    message = json.loads(event['Records'][0]['Sns']['Message'])
    bucket = message['Bucket']
    key = message['Key']
    i_d = str(message['id'])

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")
    table = dynamodb.Table('Traitify')

    table.update_item(Key={'CandidateId': i_d},UpdateExpression="set tbucket = :r, tkey=:p",
    ExpressionAttributeValues={':r': bucket,':p': key})
