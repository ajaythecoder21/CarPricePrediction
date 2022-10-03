import json
import os
import boto3
import csv
import io

ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    # TODO implement
    data = json.loads(json.dumps(event))
    payload = data['data']
    #return payload
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType = 'text/csv', 
                                       Body=payload)
    result = json.loads(response['Body'].read().decode())
    return result
