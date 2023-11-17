import json
import boto3

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):
    tasks = [item.get('title').get('S') for item in dynamodb_client.scan(TableName='Tasks')['Items']]
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'tasks': tasks,
        })
    }
