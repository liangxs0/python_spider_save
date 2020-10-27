import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['dynamic5.scrape.center']
    start_urls = ['http://dynamic5.scrape.center/']

    def start_requests(self):
        self.base_url = "https://dynamic5.scrape.center/page/{page}"
        for page in range(1,3):
            url = self.base_url.format(page=page)
            yield scrapy.Request(url=url, callback=self.pa_my)

    def parse(self, response):
        self.logger.debug(response.text)
    def pa_my(self, response):
        pass

