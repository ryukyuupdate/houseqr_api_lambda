from urllib import request, parse
import json
import base64
import io
import cgi
import time
import my_mysql
import my_api



def lambda_handler(event, context):
    fp = io.BytesIO(base64.b64decode(event['body']))
    environ = {'REQUEST_METHOD': 'POST'}
    headers = {
        'content-type': event['headers']['content-type'],
        'content-length': event['headers']['content-length'],
    }
    
    form = cgi.FieldStorage(fp=fp, environ=environ, headers=headers)

    request_doby_data = {}
    for f in form.list:
        request_doby_data[str(f.name)] = f.value
    
    request_url_path = event['path']
    return_body_data = my_api.distribution(
        request_url_path = request_url_path,
        request_body_data = request_doby_data
    )
    
    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'application/json',
            'Access-Control-Allow-Origin': '*',
            "Content-Type": "application/json; charset=utf-8",
        },
        'body': json.dumps(return_body_data)
    };
    return response
