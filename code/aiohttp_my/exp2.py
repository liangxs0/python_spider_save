import asyncio
import requests
import time
import aiohttp

start_time = time.time()

async def get(url):
    session = aiohttp.ClientSession()#构建aiohttp的client对象
    response = await session.get(url)
    await response.text()
    await session.close()
    return response
async def request():
    url = "http://books.toscrape.com/catalogue/page-2.html"
    print(f"waiting for {url}")
    response = await get(url)
    print(f"get response for {url}")

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end_time = time.time()
print("cost time:",end_time - start_time)
