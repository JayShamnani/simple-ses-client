import json
import boto3
import os

def lambda_handler(event, context):
    
    cognito = boto3.client('cognito-idp')
    
    response = dict()
    
    if not 'session' in event and not 'username' in event and not 'new_password' in event:
        response['statusCode'] = 400
        response['errorCode'] = 'BadRequest'
        response['error'] = 'Missing fields in request'
        return response
        
    username = event['username']
    new_password = event['new_password']
    session = event['session']
    
    try:
        
        client_response = cognito.respond_to_auth_challenge(
            ClientId=os.environ['CLIENT_ID'],
            ChallengeName='NEW_PASSWORD_REQUIRED',
            Session=session,
            ChallengeResponses={
                'USERNAME': username,
                'NEW_PASSWORD': new_password
            }
        )
        response['statusCode'] = 200
        response['response'] = client_response
        
    except Exception as e:
        
        print(e)
        response['statusCode'] = 500
    
    print(json.dumps(response))
    
    return response
