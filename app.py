from llama_index import LLMPredictor, StorageContext, ServiceContext, load_index_from_storage
# from langchain.chat_models import ChatOpenAI
from llama_index.llms import OpenAI
import openai

def query_index(query):

    # Rebuild local store context
    storage_context = StorageContext.from_defaults(persist_dir="storage")

    # Define LLM - default is gpt 3.5 turbo, just adding it in here for reference t change later
    # llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", max_token=512, streaming=True))
    # service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    # Set custom LLM model : llam_index 0.7.0 +
    llm = OpenAI(temperature=0, model="gpt-3.5-turbo")
    service_context = ServiceContext.from_defaults(llm=llm)

    # Load index
    index = load_index_from_storage(storage_context, service_context=service_context)

    #Pass streaming=True in the below function to enable streaming
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print(response)
    print(response.get_formatted_sources())

question = input("Ask me something:")
query_index(question)