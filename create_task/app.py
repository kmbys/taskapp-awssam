import json
import boto3
import os
import uuid

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    table_name = os.environ['TABLE_NAME']

    id = str(uuid.uuid4())

    body = json.loads(event['body'])

    dynamodb_client.put_item(
        TableName=table_name,
        Item={
            'id': { 'S': id },
            'title': { 'S': body['title'] },
            'description': { 'S': body['description'] },
        }
    )

    return {
        'statusCode': 201,
        'headers': {
            'Location': f'/tasks/{id}'
        }
    }
