from elasticsearch import Elasticsearch, helpers

from settings import ES_BASE_CONF, LOCAL_ES_INDEX


es = Elasticsearch(ES_BASE_CONF["localhost"]["host"])
# q = {}

# es_result = helpers.scan(
#     client=es,
#     query=q,
#     scroll='1m',
#     index=LOCAL_ES_INDEX
# )
