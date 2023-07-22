import json
import boto3
from boto3 import client

def lambda_handler(event, context):
    print("event: ", event)
    s3 = boto3.resource('s3')
    input_bucket = s3.Bucket('challobucketforvideos')
    inputs = []
    channel = event['params']['path']['channel_name']
    for s3_file in input_bucket.objects.filter(Prefix=channel).all():
        inputs.append(s3_file.key)
        
    temp = []
    
    for keys in inputs:
        if keys.endswith('.ts'):
            d = {}
            d['Key'] = keys
            temp.append(d)
    
    
    print(temp)
    
    client = boto3.client('elastictranscoder', region_name = 'ap-southeast-1')
    job = client.create_job(
        PipelineId = '', #Add your pipeline id here 
        Inputs=temp,
        Output={'Key': channel + '.mp4', 'PresetId': '1351620000001-000010'
        }
    )
    return {
        'statusCode': 200
    }