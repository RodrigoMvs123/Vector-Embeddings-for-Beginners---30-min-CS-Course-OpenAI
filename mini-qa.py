ASTRA_DB_BUNDLE_PATH="C:\Users\Matheus\Desktop\Rodrigo\Visual Studio Code\Ania Kubow\Vector Embeddings for Beginners - 30 min CS Course  OpenAI\search-python\secure-connect-vector-database.zip"
ASTRA_DB_APPLICATION_TOKEN="AstraCS:zOhFuwhgurjebZbUwQoNKZxB:1327a178849314f6dc31d32e84de44e9bcb2abeed1105317c18382b6426c02b6"
ASTRA_DB_CLIENT_ID=""
ASTRA_DB_CLIENT_SECRETE="" 
ASTRA_DB_KEYSPACE="search"
OPEN_AI_KEY="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"

from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from datasets import load_dataset 

cloud_config= {
'secure_connect_bundle': ASTRA_DB_SECURE_BUNDLE_PATH
}
auth_provider = PlainTextAuthProvider(ASTRA_DB_CLIENT_ID,ASTRA_DB_CLIENT_SECRETE)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
astraSession = cluster.connect()

llm = OpenAI(openai_api_key=OPEN_AI_KEY)
myEmbedding = OpenAIEmbeddings(openai_api_key=OPEN_AI_KEY)

myCassandraVStore = Cassandra(
    embedding=myEmbedding,
    session=astraSession,
    keyspace=ASTRA_DB_KEYSPACE,
    table_name="qa_mini_demo",
)

print("Loading data from huggingface")
myDataset = load_dataset("Biddls/Onion_News", split="train")
headlines = myDataset["text"][:50]

print("\nGenerating embeddings and storing in AstraDB")
myCassandraVStore.add_texts(headlines)

print("Inserted %i headlines.\n" % len(headlines))

vectorIndex = VectorStoreIndexWrapper(vectorstore=myCassandraVStore)

first_question = True 
while True:
    if first_question:
        query_text = input("\nEnter your question (or type 'quit' to exit): ")
        first_question = False
    else:
        query_text = input("\nWhat is your next question (or type 'quit' to exit): ")

    if query_text.lower() == 'quit':
        break 

    print("QUESTION: \"%s\"" % query_text)
    aswer = vectorIndex.query(query_text, llm=llm).strip()
    print("ANSWER: \"s%\"\n" % answer)

    print("DOCUMENTS BY RELEVANCE:")
    for doc, score in myCassandraVStore.similarity_search_with_score(query_text, k=4):
        print(" %0.4f \"%s...\"" % (score, doc.page_content[:60]))
    



