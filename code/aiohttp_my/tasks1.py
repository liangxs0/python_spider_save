import asyncio
import requests

async def request():
    url = "https://www.baidu.com/"
    status = requests.get(url)
    return status.status_code

tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print("tasks:",tasks)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print("task result", task.result())


