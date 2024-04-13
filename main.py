import argparse
from src.model import embed_text
from src.es import upload_to_es, search_es, create_index, delete_index

def main(args):
    if args.mode == 'upload_es':
        print("Uploading to Elasticsearch mode selected. Dataset path: {}".format(args.data_path))
        upload_to_es(args.data_path, args.index_name)
        print("Data successfully uploaded to Elasticsearch.")

    elif args.mode == 'search':
        print("Search mode selected. Please enter a query:")
        query = input("Query: ")
        query_vector = embed_text(query).cpu()
        results = search_es(args.index_name, query_vector.numpy(), size=10)
        print("Search results:")
        for result in results['hits']['hits']:
            print(f"Document ID: {result['_id']}, Score: {result['_score']}, Text: {result['_source']['text']}")

    elif args.mode == 'create_index':
        print("Creating Elasticsearch index.")
        create_index(args.index_name, dimensions=384)  # Update dimensions according to your model
        print("Index created.")

    elif args.mode == 'delete_index':
        print("Deleting index.")
        delete_index(args.index_name)
        print("Index deleted.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run various model operations")
    parser.add_argument('--mode', type=str, choices=['upload_es', 'search', 'create_index', 'delete_index'], required=True, help='Select the mode of operation: upload_es, search, create_index, delete_index')
    parser.add_argument('--data_path', type=str, help='Path to the data to be uploaded to Elasticsearch')
    parser.add_argument('--index_name', type=str, default="your_index_name", help='Name of the Elasticsearch index')

    args = parser.parse_args()
    main(args)
