from aws_requests_auth.aws_auth import AWSRequestsAuth
# https://github.com/DavidMuller/aws-requests-auth
from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
import os


con_opts = {
    'ax_key': os.getenv('AWS_AX_KEY'),
    'sec_key': os.getenv('AWS_SEC_KEY'),
    'es_host': os.getenv('AWS_ES_HOST'),
    'aws_region': os.getenv('AWS_REGION'), 
    'timeout':30,
}

def connect(opts):
    '''Connect an ES client with AWSV4 signing.'''
    auth = AWSRequestsAuth(aws_access_key=opts['ax_key'],
                        aws_secret_access_key=opts['sec_key'],
                        aws_host=opts['es_host'],
                        aws_region=opts['aws_region'],
                        aws_service='es')

    es_client = Elasticsearch(host=opts['es_host'],
                            port=80,
                            connection_class=RequestsHttpConnection,
                            http_auth=auth,
                            timeout=opts['timeout'])
    return es_client

