import pytest
import json

@pytest.fixture
def app():
    from create_task import app
    return app

@pytest.fixture
def mock_os_environ(mocker):
    mocker.patch.dict('os.environ', {'TABLE_NAME': 'xxx-xxx-TaskTable-xxxx'})

@pytest.fixture
def mock_boto3_client(mocker):
    mocker.patch('boto3.client', mocker.Mock())

def test_create_task_1(mock_os_environ, mock_boto3_client, app):
    response = app.lambda_handler({ 'body': '{"title": "タスク1", "description": "タスク内容1"}' }, '')

    assert response['statusCode'] == 201
    assert response['headers']['Location'].startswith('/tasks/')
    # TODO モックが呼ばれたことの検証

def test_create_task_2(mock_os_environ, mock_boto3_client, app):
    response = app.lambda_handler({ 'body': '{ "title": "タイトルのみのタスク1" }'}, '')
    
    assert response['statusCode'] == 201
    assert response['headers']['Location'].startswith('/tasks/')
