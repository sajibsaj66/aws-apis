import requests
import json
import boto3

def image_upload(event, context):
    baseUrl = "https://robohash.org/"
    username = event['queryStringParameters']['username']
    url = baseUrl+username
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        session = boto3.Session()
        s3 = session.resource('s3')
        
        bucket_name = 'challoprofilegeneratedpics'
        key = username+'.png' # key is the name of file on your bucket
        
        bucket = s3.Bucket(bucket_name)
        bucket.upload_fileobj(r.raw, key)
        
        return {
            'statusCode': 200
        }
        
    else:
        return {
            'statusCode': 502
        }