from list_tasks import app

def test_stock_checker():
    response = app.lambda_handler(None, '')

    assert response['statusCode'] == 200
    assert 'tasks' in response['body']
