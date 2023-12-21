# TaskApp by AWS SAM
"TaskApp by AWS SAM" is a simple task-management application,
which is constructed by using AWS Lambda, DynamoDB and API Gateway,  provisioned by AWS SAM template.

# Requirement
* SAM CLI 1.99.0

# Development
## Unit Test
```
python3 -m pytest tests/unit
```

## Local Emulation
```
sam local start-api --port 8080
```

## SAM Accelerate
```
sam sync --watch --stack-name taskapp-sync --use-container
```

# Build
CloudFormation template and artifacts are created with build command.
```
sam build --use-container
```

# Deploy
CloudFormation stack is created with deploy command.
```
sam deploy --guided
```
Then, upload static files to FrontendBucket.
```
aws s3 sync public s3://{FrontendBucketName value}/ --include "*"
```

# Clean
Delete objects in FrontendBucket.

CloudFormation stack is deleted with delete command.
```
sam delete
```
