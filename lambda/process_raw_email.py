import json
from email import policy
from email.parser import BytesParser
import boto3
from uuid import uuid4
import time
import re
import os

def lambda_handler(event, context):

    print("incoming mail log")
    print("this is base event: ", event)
    
    for i in event['Records']:
        
        bucket_name = i['s3']["bucket"]["name"]
        object_key = i['s3']["object"]["key"]
        
        if not bucket_name and not object_key:
            return {
                'statusCode': 400,
                'body': json.dumps('BadEvent')
            }
        
        message_string = get_s3_object(bucket_name,object_key)
        
        print("S3 file data type ",type(message_string))
        message = BytesParser(policy=policy.default).parsebytes(message_string)
        email_keys = message.keys()
        email_values = message.values()
        email_dict = dict(zip(email_keys,email_values))
        email_dict['id'] = str(uuid4())
        email_dict['is_read'] = False
        email_dict['folder'] = ""
        email_dict['flagged'] = False
        email_dict['timestamp'] = int(time.time())
        email_dict['updated_by'] = "UNEXPRESSED_LAMBDA"
        try:
            message_body_string = message.get_body().as_string()
            regex = re.compile(r'\<[^<]+[^>]+\>', re.MULTILINE | re.IGNORECASE)
            message_body_string = re.findall(regex, message_body_string)
            message_body_string = "".join(message_body_string)
            message_body_string = message_body_string.replace("\n","")
            email_dict['body'] = message_body_string
        except Exception as e:
            email_dict['body'] = None
            print(e)
        
        print("Generated DB Data:",json.dumps(email_dict))
        put_email_in_db(email_dict)
        delete_object_from_s3(bucket_name, object_key)
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def get_s3_object(bucket_name, object_key):
    
    client = boto3.client('s3')
    response = client.get_object(Bucket=bucket_name, Key=object_key)
    response = response['Body'].read()
    return response
    
def put_email_in_db(data):

    client = boto3.resource('dynamodb')
    table = client.Table(os.environ['EMAIL_TABLE'])
    response = table.put_item(Item=data)

def delete_object_from_s3(bucket_name, object_key):

    client = boto3.client('s3')
    response = client.delete_object(Bucket=bucket_name, Key=object_key)

