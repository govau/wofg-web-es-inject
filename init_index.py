from aws_requests_auth.aws_auth import AWSRequestsAuth
# https://github.com/DavidMuller/aws-requests-auth
from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
from auth import connect
import os


if __name__ == '__main__':
    mapping_path = 'mapping.json'
    index = 'gatest'
    mapping = open(mapping_path).read()
    con_opts = {
        'ax_key': os.getenv('AWS_AX_KEY'),
        'sec_key': os.getenv('AWS_SEC_KEY'),
        'es_host': os.getenv('AWS_ES_HOST'),
        'aws_region': os.getenv('AWS_REGION'), 
        'timeout':30,
    }
    es_client = connect(con_opts)

    print('starting..')
    print('Target {}'.format(index))
    result = es_client.indices.delete(index=index, ignore=[400, 404])
    result = es_client.indices.create(index=index, ignore=400, body=mapping)
    print(result)
    print('..done.')