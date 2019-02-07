import asyncio
from aiohttp import ClientSession
import timeit

async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            r = await response.read()
            print(r)

start = timeit.default_timer()

loop = asyncio.get_event_loop()
tasks = []

url = 'http://0.0.0.0:8080?{0}'

for i in range(100):
    task = asyncio.ensure_future(hello(url.format(i)))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))

duration = timeit.default_timer()-start
print(duration)
