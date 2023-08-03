from fastapi import FastAPI
from typing import Optional
from twisted.internet import reactor
from helpers import data_loader, start_crawler, split_docs, init_database, get_full_text, search
import uvicorn



app = FastAPI()

# Base route to check if the server is running fine
@app.get("/")
def read_root():
    return {"status": "Server is running fine!"}


# Route for running the web scraper and saving JSON files
@app.get("/getLinks")
def get_links(start_url: str, allowed_domain: str, max_depth: Optional[int] = 2):
    # Start the crawler with the given parameters
    deferred = start_crawler(start_url, allowed_domain ,max_depth=5)
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
    print("data loaded")
    docs = split_docs(data)
    print("docs split")
    database = init_database(docs)
    print("database initialized")
    return {"status": "Database initialized successfully!", "database": database}

@app.get("/search")
def query(query: str, model_name: Optional[str] = "all-MiniLM-L6-v2"):
    answer = search(query,model_name)
    return {"status": "Search completed successfully!", "answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)
