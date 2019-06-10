import json
import boto3 
import urllib
from pprint import pprint
import logging 
logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

print('Loading function')
client = boto3.client('s3')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    bucket = event['Records'][0]['s3']['bucket']['name']
    objectname = event['Records'][0]['s3']['object']['key']
    version = event['Records'][0]['s3']['object']['versionId']
    listofresources = []
    listofresources.append(bucket)
    listofresources.append(objectname)
    listofresources.append(version)
    print (listofresources)
   

    #print (version)
    
    client.put_object_tagging(
        Bucket=listofresources[0],
        Key=listofresources[1],
        VersionId=listofresources[2],
        Tagging={
            'TagSet': [
                {
                    'Key': 'hell',
                    'Value': 'yeah'
                },
            ]
        }
    )
