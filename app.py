from llama_index import StorageContext, load_index_from_storage

def query_index(query):

    # Rebuild local store context
    storage_context = StorageContext.from_defaults(persist_dir="storage")

    # Load index
    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print(response)

query_index("What is llma")