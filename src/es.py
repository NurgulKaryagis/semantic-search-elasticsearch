import pandas as pd
from elasticsearch import Elasticsearch, helpers
from src.model import embed_text 
from src.data import data_loader

es = Elasticsearch("http://localhost:9200", request_timeout=30)

def create_index(index_name, dimensions=384):
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "text": {
                    "type": "text"
                },
                "embedding": {
                    "type": "dense_vector",
                    "dims": dimensions
                }
            }
        }
    }
    
    es.indices.create(index=index_name, body=settings)
    

def df_to_es(es, index_name, df):
    df_iter = df.iterrows()
    for index, document in df_iter:
        text = document['passage']  
        embedding = embed_text(text).tolist()  
        yield {
            "_index": index_name,
            "_id": f"{index}",
            "_source": {
                "text": text,
                "embedding": embedding  
            },
        }

def upload_to_es(data_path, index_name):
    df = pd.read_parquet(data_path)
    helpers.bulk(es, df_to_es(es, index_name, df))

def search_es(es, index_name, query_vector, size=10):
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                "params": {"query_vector": query_vector}
            }
        }
    }
    body = {
        "size": size,
        "query": script_query,
        "_source": ["text"]
    }
    return es.search(index=index_name, body=body)



def search_es( index_name, query_vector, size=10):
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                "params": {"query_vector": query_vector}
            }
        }
    }
    body = {
        "size": size,
        "query": script_query,
        "_source": ["text", "embedding"]
    }
    return es.search(index=index_name, body=body)


def delete_index( index_name):
    es.indices.delete(index=index_name)
