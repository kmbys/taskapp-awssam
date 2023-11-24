import json
import boto3
import os
import uuid

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    table_name = os.environ['TABLE_NAME']

    body = json.loads(event['body'])

    task = {
        'id': { 'S': str(uuid.uuid4()) },
        'title': { 'S': body['title'] },
    }
    description = body.get('description')
    if description is not None:
        task['description'] = description

    dynamodb_client.put_item(
        TableName=table_name,
        Item=task,
    )

    return {
        'statusCode': 201,
        'headers': {
            'Location': f'/tasks/{id}'
        }
    }
