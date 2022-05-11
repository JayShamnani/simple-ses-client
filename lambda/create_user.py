import json
import boto3
import os

def lambda_handler(event, context):
    '''
    create a user in the cognito user pool
    only to be used by admins
    '''

    print("create admin lambda")
    print(json.dumps(event))
    cognito = boto3.client('cognito-idp')

    response = {
        'statusCode': '',
        'body': ''
    }
    username = event['username']
    password = event['password']
    is_admin = event['is_admin']
    email = event['email']

    try:
        client_response = cognito.admin_create_user(
            UserPoolId=os.environ['USER_POOL_ID'],
            Username=username,
            TemporaryPassword=password,
            DesiredDeliveryMediums=['EMAIL'],
            ForceAliasCreation = False,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email
                },
                {
                    'Name': 'custom:admin',
                    'Value': is_admin
                },
            ]
        )
        print(client_response)
        response['body'] = json.dumps(True)
        response['statusCode'] = 200
    
    except Exception as e:
        print(e)
        response['statusCode'] = 500
        response['error'] = json.dumps(e)

    
    return response