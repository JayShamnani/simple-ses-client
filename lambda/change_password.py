import json
import boto3

def lambda_handler(event, context):
    
    cognito = boto3.client('cognito-idp')
    
    response = dict()
    
    if not 'previous_password' in event or not 'proposed_password' in event or not 'access_token' in event:
        response['statusCode'] = 400
        response['errorCode'] = 'BadRequest'
        response['error'] = 'Missing fields in request'
        return response
    
    previous_password = event['previous_password']
    proposed_password = event['proposed_password']
    access_token = event['access_token']
    
    try:
    
        client_response = cognito.change_password(
            PreviousPassword=previous_password,
            ProposedPassword=proposed_password,
            AccessToken=access_token
        )
    
        response['statusCode'] = 200
        response['response'] = client_response
        
    except Exception as e:
        
        print(e)
        response['statusCode'] = 500
    
    print(json.dumps(response))
    
    return response