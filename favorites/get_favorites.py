import os
import json

from favorites import decimalencoder
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def get_favorites(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    
    org_id = event['pathParameters']['id']

    
    result = table.query(
        
        KeyConditionExpression=Key('org_id').eq(org_id)
    )

    
    items = result.get('Items', [])

    
    response = {
        "statusCode": 200,
        "body": json.dumps(items, cls=decimalencoder.DecimalEncoder)
    }

    return response