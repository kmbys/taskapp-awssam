import json
import boto3
import os

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    task_table_name = os.environ['TASK_TABLE_NAME']

    tasks = [item.get('title').get('S') for item in dynamodb_client.scan(TableName=task_table_name)['Items']]
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'tasks': tasks,
        })
    }
