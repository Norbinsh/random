import os
import json
import boto3
from datetime import datetime, timedelta
from src.metricdata import MetricDataQuery

MAX_INT = 3
ALLOWED_PARAMS = {'last_4_weeks': 2419200, 'last_2_weeks': 1209600,\
    'last_week': 604800, 'last_24_hours': 86400}

def handler(event, context):
    sts_creds = assume_role(os.environ['CROSS_ACCOUNT_ROLE_ARN'], os.environ['session_name'])
    access_key, secret_access, session_token = sts_creds['Credentials']['AccessKeyId'],\
         sts_creds['Credentials']['SecretAccessKey'],\
                sts_creds['Credentials']['SessionToken']

    client = boto3.client('cloudwatch', aws_access_key_id = access_key,
        aws_secret_access_key = secret_access,
        aws_session_token = session_token
        )
    
    try:
        time_period = event['queryStringParameters']['time_period']
    except Exception:
        return {"statusCode": 400, "body": "Bad Request"}
    
    if time_period not in ALLOWED_PARAMS.keys():
        return {"statusCode": 400, "body": "Bad Request"}
    
    start_time = datetime.utcnow() - timedelta(seconds=ALLOWED_PARAMS[time_period])
    end_time = datetime.utcnow()

    response = client.get_metric_data(
        MetricDataQueries=MetricDataQuery,
        StartTime=start_time,
        EndTime=end_time,
        ScanBy='TimestampAscending'
    )

    data_points_values = response['MetricDataResults'][0]['Values']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "start_time": str(start_time),
            "end_time": str(end_time),
            "uptime": f"{(sum(data_points_values) / len(data_points_values) / MAX_INT) * 100:.2f}"
            })
    }

def assume_role(cross_account_role_arn, session_name):
    client = boto3.client('sts')
    sts_response = client.assume_role(
        RoleArn=cross_account_role_arn, RoleSessionName=session_name, DurationSeconds=900
    )
    return sts_response
