import os
import json
import urllib3

def lambda_handler(event, context):
    url = event.get('issue').get('html_url')

    http = urllib3.PoolManager()
    
    r = http.request(
        'POST',
        os.getenv('SLACK_URL'),
        headers={'Content-Type': 'application/json'},
        body=json.dumps({
            'text': f'Issue Created: {url}',
        }),
    )
    
    return r.read().decode('utf-8')
