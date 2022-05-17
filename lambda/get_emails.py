import json
import boto3
import os

def lambda_handler(event, callback):
    
    response = dict()
    response['headers'] = {'Content-Type': 'application/json'}
    
    _body = json.loads(event['body'])
    _cognito_response = ''
    
    if 'access_token' not in _body:
        response['statusCode'] = 400
        response['errorMessage'] = 'Access Token not found in request'
        response['error'] = 'BadRequest'
        return response
    
    try:
        client = boto3.client('cognito-idp')
        _cognito_response = client.get_user(
            AccessToken= _body['access_token']
        )
    
    except client.exceptions.NotAuthorizedException as e:
        response['body'] = json.dumps(e.__dict__['response'])
        response['statusCode'] = 403
        return response
    
    except client.exceptions.UserNotFoundException as e:
        response['body'] = json.dumps(e.__dict__['response'])
        response['statusCode'] = 404
        return response
    
    except Exception as e:
        print(e)
        response['body'] = json.dumps({'ErrorMessage': 'Unknown Error'})
        response['statusCode'] = 500
        return response
    
    dynamodb_client = boto3.client('dynamodb')
    paginator = dynamodb_client.get_paginator('query')
    
    PaginationConfig = dict()
    PaginationConfig['MaxItems'] = _body['MaxItems'] if 'MaxItems' in _body else int(os.environ['MAX_ITEMS'])
    PaginationConfig['PageSize'] = _body['PageSize'] if 'PageSize' in _body else int(os.environ['PAGE_SIZE'])
    PaginationConfig['StartingToken'] = _body['StartingToken'] if 'StartingToken' in _body else None
    
    response_iterator = paginator.paginate(
        TableName=os.environ['EMAIL_TABLE'],
        KeyConditions={
            'username': {
                'AttributeValueList': [
                    {
                        'S': _cognito_response['Username'],
                    },
                ],
                'ComparisonOperator': 'EQ'
            }
        },
        PaginationConfig=PaginationConfig
        
        )
    
    print(response_iterator.build_full_result())
    return {
        'statusCode': 200,
        'body': json.dumps(response_iterator.build_full_result())
    }
