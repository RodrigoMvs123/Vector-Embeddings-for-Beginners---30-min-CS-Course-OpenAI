

## Vector-Embeddings-for-Beginners---30-min-CS-Course-OpenAI

https://www.youtube.com/watch?v=PR7xz5vQKGg 

https://raw.githubusercontent.com/RodrigoMvs123/Vector-Embeddings-for-Beginners---30-min-CS-Course-OpenAI/main/README.md

https://github.com/RodrigoMvs123/Vector-Embeddings-for-Beginners---30-min-CS-Course-OpenAI/blame/main/README.md

## Vector Embeddings 
Vector embedding is a popular technique to represent information in a format that can be easily processed by algorithms, especially deep learning models. This ‘information’ can be text, pictures, video and audio.

```
Word/Text Embeddings
Document Embeddings
Sentence Embeddings 
Graph Embeddings
Image Embeddings
```
```
Recommendation systems
Anomaly Detection
Transfer learning
Visualisations
Information retrieval 
Audio + speech processing
Facial recognition 
```

Text Embeddings

food 
```
[
0.0233…
1436 more items
]
```

Semantics

The branch of linguistics and logic concerned with meaning

OpenAI
- https://openai.com/ 

API
```
Integrate OpenAI models into your application or business 
View API Key
Create new secret key
Name
demo-key 
Create secret key
“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”
Copy 
Done
```

API reference

Embeddings 
```
Create embedding
Request body
Example request ( Copy and Paste on Prompt )
Response  ( Copy and Paste on Prompt )
```


Prompt
```
aniakubow@Anias-MBP ~ % curl https://api.openai.com/v1/embeddings \
-H “Authorization: Bearer “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” \
-H “Content-type: application/json” \
-d ‘{
    “input”: “The food was delicious and the waiter…”,
    “model”: “text-embedding-ada-002”
}’

{           
            “object”: “list”,
            “data”: [
                {
           …
       { 
]
aniakubow@Anias-MBP ~ % 
```

Prompt
```
aniakubow@Anias-MBP ~ % curl https://api.openai.com/v1/embeddings \
-H “Authorization: Bearer “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” \
-H “Content-type: application/json” \
-d ‘{
    “input”: food”,
    “model”: “text-embedding-ada-002”
}’

{           
            “object”: “list”,
            “data”: [
                {
           …
       { 
]
aniakubow@Anias-MBP ~ % 
```

Vector and Databases

Setting up

Datastax
- https://www.datastax.com/  ( Login in ) 

```
Database
Create database
Database name
vector_database ( Active )
            Keyspace Name
search
Region 
us-east1
Create Database
```

Langchain ( https://www.langchain.com/ )

An open source network that allows AI developers to have better interactions with several large language models (LLMs).

https://python.langchain.com/docs/modules/data_connection/


AI Assistant
```
vector_database
Active
2c8de08a-3140-4aa0-8723-2ffe406d8898
```
vector-enabled


Connect
```
Get an application token 
```
```
Generate Token 
{ "clientId": "zOhFuwhgurjebZbUwQoNKZxB" "secret": "mFwrYs6n7vrmL9y0OZtCmHazbYypFQiKDa2YXPvW+N62L1PXE._OcrfBrzO.NJr9wetYKaUmoNXRATzZt53EkZ1QG+JK-TOa+-cb4AKnXp5pJFaZoSzOEw5EG3.zCtpF" "token": "AstraCS:zOhFuwhgurjebZbUwQoNKZxB:1327a178849314f6dc31d32e84de44e9bcb2abeed1105317c18382b6426c02b6" }
```

Get a Secure Connect Bundle

us-east1

OpenAI
- https://openai.com/ 

API
```
Integrate OpenAI models into your application or business 
View API Key
Create new secret key
Name
demo 
… ( copy and past )
```

Prompt

Change Directories 
```
aniakubow@Anias-MBP ~ % cd WebstormProjects
aniakubow@Anias-MBP WebstormProjects % mkdir search-python
aniakubow@Anias-MBP WebstormProjects % cd search-python
aniakubow@Anias-MBP search-python % code .
```

## Source code
```python
Visual Studio Code
EXPLORER 
OPEN EDITORS
SEARCH-PYTHON
.venv
index.py

index.py
print('Hello')
```

Python: Create Environment 
```
Venv Creates a `.venv` virtual environment in the current workspace 
Python 3.10.11 64-bit(microsoft store)~\AppData\Local\Microsoft\WindowsApps\python3.10.11.64-bit
```

### Visual Studio Code 
Terminal
```bash
> Hello
pip install cassio datasets langchain openai tiktoken
```

## Source Code
```python
Visual Studio Code
EXPLORER 
OPEN EDITORS
SEARCH-PYTHON
.venv
mini-qa.py

mini-qa.py
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
```

