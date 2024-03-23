import json
import logging
import os
import datetime
import boto3

dynamodb = boto3.resource('dynamodb')

def add_favorite(event, context):
    try:
        data = json.loads(event['body'])
        org_id = event['pathParameters']['id']

        if 'favourite_org_id' not in data:
            logging.error("Validation Failed")
            raise Exception("Couldn't create the favorite item.")
        
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
        item = {
            'org_id': org_id,
            'favourite_org_id': data['favourite_org_id'],
            'date': timestamp,
        }
        
        table.put_item(Item=item)
        
        response = {
            "statusCode": 201,
            "body": json.dumps(item)
        }

    except json.JSONDecodeError as e:
        logging.error(f"Error al cargar los datos JSON: {e}")
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": "Error al cargar los datos JSON"})
        }

    except KeyError as e:
        logging.error(f"Error de clave faltante: {e}")
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": "Se esperaba un parámetro faltante"})
        }

    except Exception as e:
        logging.error(f"Error desconocido: {e}")
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": "Se ha producido un error"})
        }

    return response
