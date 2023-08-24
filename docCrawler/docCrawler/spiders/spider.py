import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json
from urllib.parse import urlparse

class DocSpider(CrawlSpider):
    name = 'DocSpider'
    allowed_domains = []
    max_depth = 1  # Set the maximum depth to 5
    links = set()
    
    def __init__(self, start_url: str, *args, **kwargs):
        super(DocSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.allowed_domains = [urlparse(start_url).netloc]
        
    rules = (
        Rule(LinkExtractor(allow=(), unique=True), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        new_links = set()  # Initialize the link set for the current page
        for link in LinkExtractor().extract_links(response):  # Extract links from all domains
            if self.start_urls[0] in link.url:  # Check if the link's domain is allowed
                new_links.add(link.url)
        
        # Add new links to the main links set
        self.links.update(new_links)

        # Follow other links on the page if depth allows
        depth = response.meta.get('depth', 0)
        if depth < self.max_depth:
            for next_link in new_links:
                yield scrapy.Request(next_link, callback=self.parse_item, meta={'depth': depth + 1})

    def closed(self, reason):
        # Save the scraped data to JSON when the spider is closed
        data = {"links": list(self.links)}
        self.save_to_json(data)
        return
  
    def save_to_json(self, data):
        with open('./files/output_links.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
