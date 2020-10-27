import asyncio
async def execute(x):
    print(x)
coroutine = execute(1)
print("构造协程对象")
loop = asyncio.get_event_loop()#循环事件对象
task = loop.create_task(coroutine)#注册任务
loop.run_until_complete(task)#将协程对象注册到事件循环中并将其执行
print("end")