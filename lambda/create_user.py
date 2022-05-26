import json
import boto3
import os

def lambda_handler(event, callback):
    
    '''
    create a user in the cognito user pool
    only to be used by admins
    '''
    
    '''
    TODO:
    - validate user request is from an admin
    '''


    print(json.dumps(event))
    cognito = boto3.client('cognito-idp')
    event = json.loads(event['body'])
    
    response = dict()
    response['headers'] = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Request-Method': ' OPTIONS, POST',
        'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
    }
    
    username = event['username'] if 'username' in event and len(event['username']) > 1 else ''
    password = event['password'] if 'password' in event and len(event['password']) > 1 else ''
    is_admin = event['is_admin'] if 'is_admin' in event else 'FALSE'
    email = event['email'] if 'email' in event and len(event['email']) > 1 else ''
    phone_number = event['phone_number'] if 'phone_number' in event and len(event['phone_number']) > 1 else ''
    given_name = event['first_name'] if 'first_name'  in event and len(event['first_name']) > 1 else ''
    family_name = event['last_name'] if 'last_name'  in event and len(event['last_name']) > 1 else ''

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
                {
                    'Name': 'given_name',
                    'Value': given_name
                },
                {
                    'Name': 'family_name',
                    'Value': family_name
                },
                {
                    'Name': 'phone_number',
                    'Value': phone_number
                },
            ]
        )
        response['body'] = json.dumps(client_response, indent=4, sort_keys=True, default=str)
        response['statusCode'] = 200
        return response
    
    except cognito.exceptions.InvalidPasswordException as e:
        response['statusCode'] = 400
        response['body'] =  {
            'error' : json.dumps(e.__dict__['response'], indent=4, sort_keys=True, default=str),
            'errorMessage':'Invalid Password',
            'errorCode':'InvalidPasswordException'
            }
        return response
    
    except cognito.exceptions.UsernameExistsException as e:
        response['statusCode'] = 400
        response['body'] =  json.dumps({
            'error' : json.dumps(e.__dict__['response'], indent=4, sort_keys=True, default=str),
            'errorMessage':'Username Already Exists',
            'errorCode': 'UsernameExistsException'
            })
        return response
    
    except cognito.exceptions.NotAuthorizedException as e:
        response['statusCode'] = 403
        response['body'] =  json.dumps({
            'error' : json.dumps(e.__dict__['response'], indent=4, sort_keys=True, default=str),
            'errorMessage':'User Is Not Authorized To Perform This Action',
            'errorCode':'NotAuthorizedException'
            })
        return response
        
    except cognito.exceptions.InvalidParameterException as e:
        response['statusCode'] = 400
        response['body'] =  json.dumps({
            'error' : json.dumps(e.__dict__['response'], indent=4, sort_keys=True, default=str),
            'errorMessage':'Invalid Parameter in Request',
            'errorCode':'InvalidParameterException'
            })
        return response
    
    except cognito.exceptions.InternalErrorException as e:
        response['statusCode'] = 500
        response['body'] =  json.dumps({
            'error' : json.dumps(e.__dict__['response'], indent=4, sort_keys=True, default=str),
            'errorMessage':'Internal Error Exception',
            'errorCode':'InternalErrorException'
            })
        return response
    
    except Exception as e:
        print(e)
        response['statusCode'] = 500
        response['body'] =  json.dumps({
            'errorMessage':'Unknown Error',
            'errorCode':'UnknownError'
            })
        return response