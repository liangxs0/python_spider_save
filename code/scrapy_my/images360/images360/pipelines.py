# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class Images360Pipeline:
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):
    def __init__(self, mongo_url, momgo_db):
        self.mongo_url = mongo_url
        self.mongo_db = momgo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_url=crawler.settings.get("MONGO_URL"),
                   momgo_db=crawler.settings.get("MONGO_DB"))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        name = item.collection
        self.db[name].insert(dict(item))
        return item

class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        fil_name = url.split("/")[-1]
        print(fil_name)
        return fil_name

    def item_completed(self, results, item, info):
        print(results)
        image_paths = [x["path"] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Image Download Error")
        return item

    def get_media_requests(self, item, info):
        print("_"*30)
        print(item["url"])
        yield Request(item["url"])