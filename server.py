from fastapi import FastAPI
from typing import Optional
from twisted.internet import reactor
from helpers import data_loader, start_crawler, split_docs, init_database, get_full_text, search_similarity
import uvicorn



app = FastAPI()

# Base route to check if the server is running fine
@app.get("/")
def read_root():
    return {"status": "Server is running fine!"}


# Route for running the web scraper and saving JSON files
@app.get("/getLinks")
def get_links(start_url: str, max_depth: Optional[int] = 5):
    # Start the crawler with the given parameters
    deferred = start_crawler(start_url ,max_depth=max_depth)
    # Run the Twisted reactor (start the crawling process)
    reactor.run()
    # Return any necessary response
    return {"status": "Web scraper ran successfully!"}


# Route for running function get_full_text
@app.get("/getText")
def get_text(path: Optional[str] = "output_links.json"):
    full_text = get_full_text(path)
    return {"status": "Full text generated successfully!"}


# Route for initializing the database
@app.get("/initializeDB")
def initialize_db():
    data = data_loader()
    docs = split_docs(data)
    database = init_database(docs)
    return {"status": "Database initialized successfully!", "database": database}

@app.get("/search")
def query(query: str, openai_api_key: str, model_name: Optional[str] = "all-MiniLM-L6-v2"):
    answer = search_similarity(query, openai_api_key)
    return {"status": "Search completed successfully!", "answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)
