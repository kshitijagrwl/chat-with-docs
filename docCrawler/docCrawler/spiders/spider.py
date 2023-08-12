import scrapy
import json
from urllib.parse import urljoin

class DocSpider(scrapy.Spider):
    name = 'DocSpider'
    start_urls = []  # Replace with the URL you want to start crawling from
    allowed_domains = []
    max_depth = 5
    
    def __init__(self, start_url:str , allowed_domain:str, max_depth:int, *args, **kwargs):
        super(DocSpider, self).__init__(*args, **kwargs)
        self.start_urls.append(start_url)
        self.allowed_domains.append(allowed_domain)
        self.max_depth = max_depth       
        
    def parse(self, response):
        # Extract links containing "docs"
        links = set()
        links.add(self.start_urls[0])
        for link in response.css('a::attr(href)').getall():
            if 'docs' in link:
                if link.startswith('/'):
                    link = response.urljoin(link)
                links.add(link)

        # Save the data to JSON
        data = {response.url: list(links)}
        self.save_to_json(data)

        # Follow other links on the page if depth allows
        depth = response.meta.get('depth', 0)
        if depth < self.max_depth:
            for next_link in links:
                yield scrapy.Request(next_link, callback=self.parse, meta={'depth': depth + 1})

    def save_to_json(self, data):
      with open('./files/output_links.json', 'w') as json_file:  # Use 'w' mode to overwrite the file
        json.dump(data, json_file, indent=4)
