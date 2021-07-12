import json
import logging
import os

import boto3
from botocore.exceptions import ClientError

USER_STORAGE_URL = 'https://docapi.serverless.yandexcloud.net/ru-central1/b1gvrkfc5lbadse8lj14/etn00pjqmtnlsolb0o1l'
AWS_ACCESS_KEY_ID = 'DsonMXBBADMfBIyMNSCu'
AWS_SECRET_ACCESS_KEY = 'dPBBqLJ_wgVh7GQlNZJRhCFwKNHBALd0xZB60hwZ'

def read_line(dt, dynamodb=None):
    if not dynamodb:
        print('not dynamodb')
        dynamodb = boto3.resource(
                'dynamodb',
                endpoint_url=os.environ.get(USER_STORAGE_URL),
                region_name = 'ru-central1',
                aws_access_key_id = os.environ.get(AWS_ACCESS_KEY_ID),
                aws_secret_access_key = os.environ.get(AWS_SECRET_ACCESS_KEY)
                )
    print('exec table')
    table = dynamodb.Table('data')
    print('table OK')
    print(table)
    try:
        #print('exec try')
        response = table.get_item(Key={'dt': dt})
        #print('try OK')
    except ClientError as e:
        print('exec ClientError')
        print(e.response['Error']['Message'])
    else:
        print('return')
        return response

def run():
# подключение проверено
    dynamodb = boto3.resource(
                'dynamodb',
                endpoint_url = USER_STORAGE_URL,
                region_name = 'ru-central1',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY
                )
# подключение работает
    print('Connection OK')
    #print(os.environ.get(USER_STORAGE_URL))
    user_query = read_line(20210608144541, dynamodb)
    print('Read OK')

if __name__ == '__main__':
    run()
