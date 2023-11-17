import json
import boto3

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'body': json.dumps({
            'tasks': dynamodb_client.scan(
                TableName='Tasks',
            )['Items']
        })
    }
