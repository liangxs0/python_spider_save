import scrapy
from scrapy import Spider, Request
from urllib.parse import urlencode
import json
from ..items import ImageItem
from scrapy.utils.request import request_fingerprint

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        data = {
            "ch":"phtography",
            "listype":"new"
        }
        base_url = "https://image.so.com/zjl?"
        for page in range(1, self.settings.get("MAX_PAGE")):
            data["sn"] = page*30
            params = urlencode(data)
            url = base_url + params
            self.logger.debug(f"s:{url}")
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.debug(f"res:{response.url}")
        self.logger.debug(f"type:{type(response.text)}")
        result = json.loads(response.text)
        for image in result.get("list"):
            item = ImageItem()
            item["id"] = image.get("id")
            item["url"] = image.get("qhimg_url")
            item["title"] = image.get("title")
            item["thumb"] = image.get("qhimg_thumb")
            yield item

