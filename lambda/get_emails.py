import json
import boto3
import os
from boto3.dynamodb.types import TypeDeserializer

def ddb_deserialize(r, type_deserializer = TypeDeserializer()):
    return type_deserializer.deserialize({"M": r})
    

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return (str(o) for o in [o])
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, callback):
    
    response = dict()
    response['headers'] = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Request-Method': ' OPTIONS, POST',
        'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
        
    }
    
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
    
    items = response_iterator.build_full_result()
    parsed_response = [ ddb_deserialize(r) for r in items['Items'] ]
    
    response['body'] = json.dumps(parsed_response, indent=4, sort_keys=True, default=str, cls=DecimalEncoder)
    response['statusCode'] = 200
    print(response)
    return response
