import os
import json

from favorites import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

def get_favorites(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch from the database
    result = table.query(
        Key={
            'org_id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response