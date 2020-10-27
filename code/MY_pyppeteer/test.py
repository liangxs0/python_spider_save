import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
import time
width, height = 1920,1080

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({"width":width,"height":height})
    await page.goto("https://dynamic2.scrape.cuiqingcai.com/")
    await page.waitForSelector(".item .name")
    time.sleep(5)
    await page.screenshot(path="html.png")
    doc = pq(await page.content())
    name = [item.text() for item in doc(".item .name").items()]
    print(name)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

