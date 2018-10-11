from aws_requests_auth.aws_auth import AWSRequestsAuth
# https://github.com/DavidMuller/aws-requests-auth
from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
import os


con_opts = {
    'ax_key': os.getenv('AWS_AX_KEY'),
    'sec_key': os.getenv('AWS_SEC_KEY'),
    'es_host': 'search-webcrawler-2outiqin36fsbeimp7j6p6vmna.ap-southeast-2.es.amazonaws.com',
    'aws_region':'ap-southeast-2', 
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

