import streamlit as st
from twisted.internet import reactor
import json
from docCrawler.docCrawler.spiders.spider import DocSpider
from scrapy.crawler import CrawlerRunner
from helpers import (
    start_crawler,
    get_full_text,
    split_docs,
    data_loader,
    init_database,
    search_similarity
)

st.title("Document Processing App")

# Sidebar
st.sidebar.header("Crawling Parameters")
start_url = st.sidebar.text_input("Start URL")
allowed_domain = st.sidebar.text_input("Allowed Domain")
max_depth = st.sidebar.number_input("Max Depth", value=5, min_value=1)

# Start crawling
if st.sidebar.button("Start Crawling"):
    st.sidebar.text("Crawling in progress...")
    runner = CrawlerRunner()
    # Start the spider with the given parameters
    runner.crawl(DocSpider, start_url = start_url, allowed_domain = allowed_domain ,max_depth=max_depth)
    st.sidebar.text("Crawling completed!")

# Summarize and split documents
if st.button("Process Documents"):
    get_full_text()
    st.text("Documents processed successfully!")

    st.sidebar.header("Document Splitting Parameters")
    chunk_size = st.sidebar.number_input("Chunk Size", value=500, min_value=100)
    chunk_overlap = st.sidebar.number_input("Chunk Overlap", value=20, min_value=0)

    st.sidebar.text("Splitting documents...")
    documents = data_loader()
    split_documents = split_docs(documents, chunk_size, chunk_overlap)
    st.sidebar.text("Documents split successfully!")

    st.sidebar.header("Vector Database Initialization")

    init_database(split_documents)
    st.sidebar.text("Database initialized!")

# Similarity search
st.header("Similarity Search")
query = st.text_input("Enter your query")
openai_api_key = st.text_input("OpenAI API Key")

if st.button("Search"):
    answer = search_similarity(query, openai_api_key)
    st.text("Answer:")
    st.write(answer)
