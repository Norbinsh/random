'''Custom generic CloudFormation resource example'''

import json
import logging
import signal
import secrets
import boto3
import os
from botocore.vendored import requests

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
TABLE = os.environ['DYNAMODB_TABLE']

def generate_token():
    return secrets.token_hex(16)

def handler(event, context):
    '''Handle Lambda event from AWS'''
    # Setup alarm for remaining runtime minus a second
    signal.alarm((context.get_remaining_time_in_millis() // 1000) - 1)
    try:
        LOGGER.info('REQUEST RECEIVED:\n %s', event)
        LOGGER.info('REQUEST RECEIVED:\n %s', context)
        if event['RequestType'] == 'Create':
            dynamodb = boto3.client('dynamodb')
            dynamodb.put_item(TableName=TABLE, Item={'customer': {'S': 'master'},\
                'token':{'S':generate_token()}})
            LOGGER.info('CREATE!')
            send_response(event, context, "SUCCESS",
                          {"Message": "Resource creation successful!"})
        elif event['RequestType'] == 'Update':
            LOGGER.info('UPDATE!')
            send_response(event, context, "SUCCESS",
                          {"Message": "Resource update successful!"})
        elif event['RequestType'] == 'Delete':
            LOGGER.info('DELETE!')
            send_response(event, context, "SUCCESS",
                          {"Message": "Resource deletion successful!"})
        else:
            LOGGER.info('FAILED!')
            send_response(event, context, "FAILED",
                          {"Message": "Unexpected event received from CloudFormation"})
    except: #pylint: disable=W0702
        LOGGER.info('FAILED!')
        send_response(event, context, "FAILED", {
            "Message": "Exception during processing"})


def send_response(event, context, response_status, response_data):
    '''Send a resource manipulation status response to CloudFormation'''

    response_body = json.dumps({
        "Status": response_status,
        "Reason": "See the details in CloudWatch Log Stream: " + context.log_stream_name,
        "PhysicalResourceId": context.log_stream_name,
        "StackId": event['StackId'],
        "RequestId": event['RequestId'],
        "LogicalResourceId": event['LogicalResourceId'],
        "Data": response_data
    })

    headers = {
        'Content-Type': '',
        'Content-Length': len(response_body),
    }

    LOGGER.info('ResponseURL: %s', event['ResponseURL'])
    LOGGER.info('ResponseBody: %s', response_body)

    r = requests.put(event['ResponseURL'], data=response_body, headers=headers)

    LOGGER.info("Status code: %s", r.status_code)
    LOGGER.info("Status message: %s", r.text)


def timeout_handler(_signal, _frame):
    '''Handle SIGALRM'''
    raise Exception('Time exceeded')


signal.signal(signal.SIGALRM, timeout_handler)