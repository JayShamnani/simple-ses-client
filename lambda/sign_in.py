import json
import boto3
import os

def lambda_handler(event, context):
    
    cognito = boto3.client('cognito-idp')
    
    response = dict()
    
    if not 'username' in event or not 'password' in event:
        response['statusCode'] = 400
        response['errorCode'] = 'BadRequest'
        response['error'] = 'Missing fields in request'
        return response
        
    username = event['username']
    password = event['password']
    
    response = cognito.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        },
        ClientId=os.environ['CLIENT_ID']
    )
    
    print(json.dumps(response))
    
    return response
