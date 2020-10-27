import asyncio
import aiohttp

proxy = "http://127.0.0.1:8080"
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://httpbin.org/get",proxy=proxy) as response:
            print(await response.text())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())