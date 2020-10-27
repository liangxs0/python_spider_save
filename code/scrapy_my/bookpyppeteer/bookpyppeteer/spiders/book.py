import scrapy
from gerapy_pyppeteer import PyppeteerRequest

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['dynamic5.scrape']
    start_urls = ['http://dynamic5.scrape/']
    base_url = "https://dynamic5.scrape.center/page/{page}"
    max_page = 10

    def start_requests(self):
        for page in range(1,self.max_page+1):
            url = self.base_url.format(page=page)
            yield PyppeteerRequest(url=url, callback=self.parse_index)
    def parse_index(self, response):
        res = response.css(".item")
        for item in res:
            name = item.css(".name::text").extract_first()
            auhtors = item.css(".authors::text").extract_first()
            name = name.strip() if name else None
            auhtors = auhtors.strip() if auhtors else None
            self.logger.info(f"{name}:{auhtors}")
            print("-"*30)
            yield {
                "name":name,
                "authors":auhtors
            }