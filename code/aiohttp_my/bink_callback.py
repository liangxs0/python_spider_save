import requests
import asyncio

async def request():
    url = "https://www.baidu.com/"
    status = requests.get(url)
    return status.status_code

def callback(task):
    print("status:",task.result())

coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print("task:",task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print("task:",task)
