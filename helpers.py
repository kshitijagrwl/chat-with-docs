import requests
import json
from aiohttp import ClientSession
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from langchain.document_loaders.json_loader import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains.question_answering import load_qa_chain
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from docCrawler.docCrawler.spiders.spider import DocSpider  # Replace 'your_project_name' with your actual project name

def start_crawler(start_url,allowed_domain,max_depth=5):
    """
    Start the crawler asynchronously using Twisted with given parameters.

    Parameters:
        start_url (str): The url you want as a starting point for your docs.
        allowed_domain (str): The domain you want to crawl.
        max_depth (int): The maximum depth you want to crawl.

    Returns:
        twisted.internet.defer.Deferred: A deferred object representing the asynchronous crawling process.
    """
    # Configure logging
    configure_logging()

    # Create a CrawlerRunner
    runner = CrawlerRunner()

    # Start the spider with the given parameters
    deferred = runner.crawl(DocSpider, start_url = start_url, allowed_domain = allowed_domain ,max_depth=max_depth)

    # Add a callback to stop the Twisted reactor once crawling is completed
    deferred.addCallback(stop_reactor)

    return deferred

def stop_reactor(_):
    """
    Callback function to stop the Twisted reactor when crawling is completed.

    Parameters:
        _: This parameter is not used.

    Returns:
        None
    """
    reactor.stop()

async def _fetch_article_summary(session, url):
    """
    Asynchronously fetch the summary of an article from a given URL.

    Parameters:
        session (aiohttp.ClientSession): An aiohttp session for making asynchronous HTTP requests.
        url (str): URL of the article.

    Returns:
        tuple: A tuple containing the article's title and full text.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()

    soup = BeautifulSoup(html, 'html.parser')

    # Find all the text on the page
    text = soup.get_text()
    return text

async def _process_links(links):
    """
    Process a list of article URLs asynchronously.

    Parameters:
        links (list): A list of article URLs.

    Returns:
        list: A list of tuples containing article titles and full texts.
    """
    async with ClientSession() as session:
        tasks = []
        for link in links:
            try:
                task = asyncio.create_task(_fetch_article_summary(session, link))
                tasks.append(task)
            except Exception as e:
                print(f"Failed to generate summary for {link}: {str(e)}")

        return await asyncio.gather(*tasks)

def get_full_text(path='./files/output_links.json'):
    """
    Process each link, generate summaries, and create a new JSON file.

    Parameters:
        path (str): Path to the JSON file containing the crawled links.

    Returns:
        None
    """
    with open(path, 'r') as json_file:
        crawled_data = json.load(json_file)

    summary_data_final = {}
    summary_data = []
    for url in crawled_data:
        links = crawled_data[url]
        # Process links asynchronously
        results = asyncio.run(_process_links(links))
        for text in results:
            summary_data.append({'text': text})
    summary_data_final['chatwithdocs'] = tuple(summary_data)

    # Save the summary data to a new JSON file
    with open('./files/summary_output.json', 'w') as json_file:
        json.dump(summary_data_final, json_file, indent=4)

def split_docs(documents,chunk_size=500,chunk_overlap=20):
    """
    Split a list of documents into smaller chunks of text.

    Parameters:
        documents (list): A list of text documents.
        chunk_size (int): Maximum size of each chunk (default: 500).
        chunk_overlap (int): Number of characters to overlap between adjacent chunks (default: 20).

    Returns:
        list: A list of split documents.
    """
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

def data_loader(path = './files/summary_output.json',jq_schema = '.chatwithdocs[].text'):
    """
    Load text data from a JSON file using a JSON Loader.

    Parameters:
        path (str): Path to the JSON file containing the data.

    Returns:
        list: A list containing the loaded text data.
    """
        
    loader = JSONLoader(file_path = path,jq_schema = jq_schema)
    data = loader.load()
    return data

def init_database(docs, model_name = "all-MiniLM-L6-v2"):
    """
    Initialize a vector database using the provided documents and model.

    Parameters:
        docs (list): A list of text documents.
        model_name (str): Name of the Sentence Transformer model (default: "all-MiniLM-L6-v2").

    Returns:
        Chroma: The initialized text database.
    """    
    embeddings = SentenceTransformerEmbeddings(model_name = model_name)
    Chroma.from_documents(docs, embeddings, persist_directory="./files/chroma_db", collection_metadata={"hnsw:space": "cosine"})
    
def search_similarity(query,openai_api_key="your openai api key", embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2"), openai_model="gpt-3.5-turbo"):
    """
    Perform a similarity search on the text database using the given query.

    Parameters:
        query (str): The query for the similarity search.
        embeddings (SentenceTransformerEmbeddings): An instance of SentenceTransformerEmbeddings
            with the desired model for generating text embeddings.
        openai_api_key (str): Your OpenAI API key for using the OpenAI language model.
        openai_model (str): The name of the OpenAI language model to use.

    Returns:
        str: The search result as an answer.
    """
    
    database = Chroma(persist_directory="./files/chroma_db", embedding_function=embeddings)
    query = query.lower()
    matching_docs = database.similarity_search(query)
    model_name = openai_model
    llm = ChatOpenAI(model_name=model_name,openai_api_key = openai_api_key)
    chain = load_qa_chain(llm, chain_type="stuff",verbose=True)
    answer =  chain.run(input_documents=matching_docs, question=query)
    return answer