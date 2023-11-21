import pytest
import json

@pytest.fixture
def app():
    from list_tasks import app
    return app

@pytest.fixture
def mock_os_environ(mocker):
    mocker.patch.dict('os.environ', {'TASK_TABLE_NAME': 'xxx-xxx-TaskTable-xxxx'})

@pytest.fixture
def mock_boto3_client(mocker):
    mocked_client = mocker.Mock()
    mocked_client().scan.return_value = {
        'Items': [
            {
                'title': {
                    'S':  'task1'
                }
            },
            {
                'title': {
                    'S': 'タスク2'
                }
            }
        ]
    }
    mocker.patch('boto3.client', mocked_client)

def test_list_tasks(mock_os_environ, mock_boto3_client, app):
    response = app.lambda_handler(None, '')

    assert response['statusCode'] == 200
    assert json.loads(response['body'])['tasks'] == ['task1', 'タスク2']
