import boto3
import json
import os
import secrets
from boto3.dynamodb.conditions import Key, Attr


TABLE = os.environ['DYNAMODB_TABLE']

def generate_token():
    return secrets.token_hex(16)

def handler(event, context):

    tmp_body = json.loads(event['body'])

    if len(tmp_body) == 1 and 'customer' in tmp_body.keys()\
        and type(tmp_body['customer'] == str):
        customer = tmp_body['customer']

        dynamodb = boto3.client('dynamodb')
        tmp_token = generate_token()
        dynamodb.put_item(TableName=TABLE, Item={'customer': {'S': customer},\
            'token':{'S':tmp_token}})

        response = {
            "statusCode": 200,
            "body": f"Customer '{customer}' token is: {tmp_token}"
        }
        
        return response
    return {"statusCode": 401, "body": "Unauthorized"}