from itertools import chain
from datetime import datetime
import time
import os
from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
try:
    from itertools import izip_longest as zip_longest
except ImportError:
    from itertools import zip_longest
try:
    import ujson as json
except ImportError:
    import json  # noqa: F401

from auth import connect


opts = {
    'index': 'gatest',
    'type': '_doc',
    'with_retry': True,
    'timeout': 30,
    'bulk_size': 400,
    'progress': False,
    'update': False,
    'delete': False,
    'id_field': False,
    'as_child': False,
    'verify_certs': False,  
}


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def bulk_builder(bulk, config):
    """Build bulk insert entries"""
    for item in filter(None, bulk):
        body = {
            '_index': config['index'],
            '_type': config['type'],
            '_source': item
        }               
        if config['id_field']:
            body['_id'] = item[config['id_field']]
            if config['as_child']:
                body['_parent'] = body['_id']
                body['_routing'] = body['_id']
        if config['update']:
            # default _op_type is 'index', which will overwrites existing doc
            body['_op_type'] = 'update' 
            body['doc'] = item
            del body['_source']           
        yield body


def json_lines_iter(fle):
    """Yield json objects from a file"""
    for line in fle:
        if isinstance(line, str):
            yield json.loads(line)
        else:
            yield json.loads(line.decode('utf-8'))
        

def single_bulk_to_es(bulk, config, attempt_retry, es):
    bulk = bulk_builder(bulk, config)
    max_attempt = 1
    if attempt_retry:
        max_attempt += 3
    for attempt in range(1, max_attempt + 1):
        print('Attempting chunk')
        try:
            z=helpers.bulk(es, bulk, chunk_size=config['bulk_size'])
            print(z[0])
        except Exception as e:
            if attempt < max_attempt:
                wait_seconds = attempt * 3
                log('warn', 'attempt [%s/%s] got Xception, will retry after %s seconds\n%s' % (attempt, max_attempt, wait_seconds, e))
                time.sleep(wait_seconds)
                continue
            log('error', 'attempt [%s/%s] Retrying failed, data not sent.' % (attempt, max_attempt))
            raise e
        if attempt > 1:
            log('info', 'attempt [%s/%s] Success! Recovered from previous error.' % (attempt, max_attempt))
        # completed succesfully
        break


def load(lines, config, es):
    bulks = grouper(lines, config['bulk_size'] * 3)
    for i, bulk in enumerate(bulks):
        if i % 100 == 0:
            print(f'Done {i} records!')
        try:
            single_bulk_to_es(bulk, config, config['with_retry'], es)
        except Exception as e:
            log('warn', 'Chunk {i} got exception ({e}) while processing'.format(e=e, i=i))


def format_msg(msg, sevirity):
    '''Simple formatting of messages'''
    return '{} {} {}'.format(datetime.now(), sevirity.upper(), msg)


def log(sevirity, msg):
    '''Simple logging display.'''
    print(format_msg(msg, sevirity))


def lc(f):
    '''Count lines in a file'''
    return sum(1 for _ in open(f).readlines())


def _json(opts, json_data_dir, es):
    '''perform a bulk insert of the .json files in json_data_dir
    into specified ES client connection'''
    print('[Starting]')
    json_lines = True
    #files = (open(f.path) for f in os.scandir(json_data_dir) if f.is_file() and not f.name.startswith('.') and f.name.endswith('.json'))
    dir_entries = [f for f in os.scandir(json_data_dir) if f.is_file() and not f.name.startswith('.') and f.name.endswith('.json') ]
    dic = { f.name : {'size':f.stat().st_size,'lines':lc(f.path)} for f in dir_entries }
    files = [open(f.path) for f in os.scandir(json_data_dir) if f.is_file() and not f.name.startswith('.') and f.name.endswith('.json')]
    for key in dic:
        print("{} -> {}".format(key, dic[key]))
    if json_lines:
        lines = chain(*(json_lines_iter(x) for x in files))
    else:
        lines = chain(*(json.load(x) for x in files))
    load(lines, opts, es)
    print('[Done]')


if __name__ == '__main__':
    json_dir = 'dtadata/gatest/'
    con_opts = {
        'ax_key': os.getenv('AWS_AX_KEY'),
        'sec_key': os.getenv('AWS_SEC_KEY'),
        'es_host': os.getenv('AWS_ES_HOST'),
        'aws_region': os.getenv('AWS_REGION'), 
        'timeout':30,
    }
    es_client = connect(con_opts)
    _json(opts, json_dir, es_client)