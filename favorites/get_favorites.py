import os
import json
import boto3
from boto3.dynamodb.conditions import Key
from favorites import decimalencoder

def get_favorites(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
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

    except KeyError as e:
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": "Se esperaba un parámetro faltante"})
        }

    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": "Se ha producido un error"})
        }

    return response