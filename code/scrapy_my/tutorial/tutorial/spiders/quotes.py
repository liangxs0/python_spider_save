import scrapy
from tutorial.items import QuoteItem
from urllib.parse import urljoin

class QuotesSpider(scrapy.Spider):
    name = 'quotes'#爬虫的名字且在整个项目中要保证唯一
    allowed_domains = ['quotes.toscrape.com']#它是允许你爬取的域名如果后续的请求的地址不在这个域名就连接会被过滤掉
    start_urls = ['http://quotes.toscrape.com/']#spider启动爬取的url列表初始的请求由它定义

    def parse(self, response):
        #它是spider的一个方法，m默认情况下被调用的start_urls里面的连接构成的请求完成下载后。返回的响应就会传递这个函数，然后进行解析，提取数据或者进行下一步的请求
        quotes = response.css(".quote")#多条信息
        for quote in quotes:
            item = QuoteItem()#构造item对象
            text = quote.css(".text::text").extract_first()
            author = quote.css(".author::text").extract_first()
            tags = quote.css(".tags .tag::text").extract()
            item["text"] = text
            item["author"] = author
            item["tags"] = tags
            yield item

        next = response.css('.pager .next a::attr("href")').extract_first()

        new_url = response.urljoin(next)
        print("-"*30)
        print(next)
        print(new_url)
        print("-" * 30)

        yield scrapy.Request(url=new_url, callback=self.parse)
