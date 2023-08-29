import subprocess
from helpers import *
import scrapy
import argparse
from scrapy.crawler import CrawlerProcess
from docCrawler.docCrawler.spiders.spider import DocSpider  # Replace with the actual module path

def main():
    parser = argparse.ArgumentParser(description="Run the Scrapy spider")
    parser.add_argument("start_url", help="The start URL for crawling")
    args = parser.parse_args()
    
    start_url = args.start_url
    max_depth = 5  # Set the desired max depth
    
    process = CrawlerProcess()

    print("Crawling started...")
    process.crawl(DocSpider, start_url=start_url, max_depth=max_depth)
    process.start()
    
    print("Crawling finished.")

if __name__ == "__main__":
    main()
