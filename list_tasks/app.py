import json
import boto3
import os

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    table_name = os.environ['TABLE_NAME']

    tasks = [item.get('title').get('S') for item in dynamodb_client.scan(TableName=table_name)['Items']]
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'tasks': tasks,
        })
    }
