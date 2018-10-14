# wofg-web-es-inject
Code for injecting metadata extracted from WARC as JSON into ElasticSearch as part of the WofG Web Reporting Service.

* `auth.py`: get an ES client connection with AWSv4 signing for use with the other tasks
* `init_index.py`: create/delete indexes with specified mapping.
* `inject.py`: insert data into specified index from a source folder containing line-delimited JSON files
* `mapping.json` : mapping of index structures.
* `util.py`: mainly for de-duplication of an existing ES index in case items were doubled up during the insertion process, contains logic for scrolling through all items in an index and could be extended to do various maintenance tasks
* `whitelist.py`: compares a line-delimited JSON file against a big list of field keys we wish to keep, dropping all other fields and writing a new line delimited JSON file.
