# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class TextPipeline():
    def __init__(self):
        self.limit = 60
    def process_item(self, item, spider):
        if item["text"]:
            if len(item["text"]) > self.limit:
                item["text"] = item["text"][0:self.limit].rstrip()+'...'

            return item
        else:
            return DropItem("miss item text")


import pymongo

class MongoPipeline():
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        '''
        用@classmethod标识，是一种依赖注入的方法，方法的参数是
        crawler，这个参数可以拿去做全局的每个配置信息在全局配置settings.py中
        进行定义MONGO_URL和MONGO_DB来指定要连接的地址和库名
        :param crawler:
        :return:
        '''
        return cls(mongo_url=crawler.settings.get("MONGO_URL"),
                   mongo_db=crawler.settings.get("MONGO_DB")
                   )
    def open_spider(self, spider):#在爬虫开之前进行的初始化操作，一般连接数据库和文件初始化等
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self,spider):#爬虫退出时执行的
        self.client.close()





