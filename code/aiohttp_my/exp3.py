import asyncio
import aiohttp
from pyquery import PyQuery
from urllib.parse import urljoin

start_url = "http://books.toscrape.com/catalogue/page-{}.html"
base_url = "http://books.toscrape.com/catalogue/"
page_size = 6
concurrency = 5
semaphore = asyncio.Semaphore(concurrency)#限定并发量
session = None

async def scrape_api(url):
    async with semaphore:
        try:
            print(f"scraping open {url}")
            async with session.get(url) as response:
                return await response.text()
        except Exception as e:
            print(f"scrape error {e}")

async def scrape_index(page):
    url = start_url.format(page)
    return await scrape_api(url)

async def urls(lis):
    return [urljoin(base_url, li(".product_pod .image_container a").attr("href")) for li in lis.items()]

async def detail_url(html):
    doc = PyQuery(html)
    lis = doc(".alert").siblings().children(".row").children(".col-xs-6")
    return await urls(lis)

async def dbsave(data):
    # clienct = db
    # db =
    collection = "lianjie"
    return await collection.update_one(
        {"id":data.get("id")},{"$set":data},upsert=True
    )

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, page_size+1)]
    results = await asyncio.gather(*scrape_index_tasks)
    detail_tasks = [asyncio.ensure_future(detail_url(result)) for result in results]
    detail_urls = await asyncio.gather(*detail_tasks)
    print(detail_urls)
    print("info...")



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())


