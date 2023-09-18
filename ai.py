from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os

#For powershell env variable setup
#$env:OPENAI_API_KEY = "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" 


documents = SimpleDirectoryReader('data').load_data()

#This is an in-memory store
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("What did author do growing up?")
print(response)



    

