from fastapi import FastAPI
from typing import Optional
from twisted.internet import reactor
from helpers import data_loader, start_crawler, split_docs, init_database, get_full_text, search
import uvicorn

data = data_loader()
docs = split_docs(data)
database = init_database(docs)
print("done")

query = "What functionalities are provided by the Users service?"
docs = database.similarity_search(query)
print(docs)