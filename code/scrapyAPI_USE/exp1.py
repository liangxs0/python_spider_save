from scrapyd_api import ScrapydAPI
scrapyd = ScrapydAPI("http://127.0.0.1:6800")
egg = open("book.egg", "rb")
scrapyd.add_version("book","V1",egg)