from auth import connect
import hashlib
import os

#combination of keys expected to yield a primary key (unique identifier)
keys_for_unique = ["DOCURL", "REPORT_ID"]
doc_hashvals = {}
# Process documents returned by the current search/scroll
def populate_duplicate_docs(hits):
    '''Populate a dictionary that represents each document ID for a given hashval for the hits in a scroll'''
    for item in hits:
        combined_key = ""
        for mykey in keys_for_unique:
            combined_key += str(item['_source'][mykey])
        _id = item["_id"]
        hashval = hashlib.md5(combined_key.encode('utf-8')).digest()
        # push id onto dict, accounting for keys that don't exist yet
        doc_hashvals.setdefault(hashval, []).append(_id)


def scroll_all_docs(es, index):
    '''Loop through all docs in index, populating the duplicate doc dictionary as you go'''
    # Make initial search request (match all)
    data = es.search(index=index, scroll='1m',  body={"query": {"match_all": {}}})
    sid = data['_scroll_id']
    scroll_size = len(data['hits']['hits'])
    print('Scroll Size: ' +str(scroll_size))
    # Before scroll, process current batch of hits
    populate_duplicate_docs(data['hits']['hits'])
    while scroll_size > 0:
        data = es.scroll(scroll_id=sid, scroll='2m')
        # Process current batch of hits
        populate_duplicate_docs(data['hits']['hits'])
        # Update the scroll ID
        sid = data['_scroll_id']
        # Get the number of results that returned in the last scroll
        scroll_size = len(data['hits']['hits'])


def remove_duplicates(es, index, doc_type='_doc',):
    # if any of the entries have more than one ID in their value, they're a duplicate and need to be processed
    for hashval, array_of_ids in doc_hashvals.items():
        if len(array_of_ids) > 1:
            print("********** Duplicate docs hash=%s **********" % hashval)
            # Get the documents that have mapped to the current hashval
            matching_docs = es.mget(index=index, doc_type=doc_type, body={"ids": array_of_ids})
            for doc in matching_docs['docs']:
                print("doc=%s" % doc)
            print("-----------------")
            # TODO: test for 'actual delete' option
            for doc in matching_docs['docs'][1:]:
                print("Removing: %s" % doc['_id'])
                es.delete(index=index, doc_type=doc_type, id=doc['_id'])
            print("")
    

if __name__ == '__main__':
    # Basic config options
    opts = {
        'index':'testv1',
    }
    # Connection options
    con_opts = {
        'ax_key': os.getenv('AWS_AX_KEY'), # populate this however you want
        'sec_key': os.getenv('AWS_SEC_KEY'), # populate this however you want
        'es_host': 'search-webcrawler-2outiqin36fsbeimp7j6p6vmna.ap-southeast-2.es.amazonaws.com',
        'aws_region':'ap-southeast-2',
        'timeout':30, 
    }
    # Create connection client to ES
    es_client = connect(con_opts)
    # scroll through index
    scroll_all_docs(es_client, opts['index'])
    # highlander all hashvals (there can only be one)
    remove_duplicates(es_client, opts['index'])