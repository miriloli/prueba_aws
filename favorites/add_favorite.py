import json
import logging
import os
import time
import boto3

dynamodb = boto3.resource('dynamodb')

def add_favorite(event, context):
    
    data = json.loads(event['body'])
    logging.error(data)
    if 'org_id' not in data or 'favourite_org_id' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the favorite item.")
    
    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    item = {
        'org_id': data['org_id'],
        'favourite_org_id': data['favourite_org_id'],
        'date': timestamp,
        
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 201,
        "body": json.dumps(item)
    }

    return response
