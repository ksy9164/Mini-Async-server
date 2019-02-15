import asyncio
import aiotools
from aiohttp import web
from multiprocessing import Value

routes = web.RouteTableDef()

log = Value('i',0)

@routes.get('/')
async def normal_handler(request):
    print ("The log is ",log.value)
    msg = "Hellow the log is "
    num = str(log.value)
    msg = msg + num
    return web.Response(text=msg)

async def display_log(pidx):
    if pidx == 0 :
        while True:
            log.value += 1
            await asyncio.sleep(1)

@aiotools.actxmgr
async def worker_main(loop, pidx, args):
    app = web.Application()
    loop = asyncio.get_event_loop()
    future = loop.create_task(display_log(pidx))
    app.add_routes(routes)

    web_handler = app.make_handler()
    server = await loop.create_server(
            web_handler,
            host='0.0.0.0',
            port =8888,
            reuse_port=True)
    try:
        yield
    finally:
        server.close()
        await server.wait_closed()
        await app.shutdown()
        await web_handler.finish_connections(60.0)
        await app.cleanup()

if __name__ == '__main__':
   # Run the above server using 4 worker processes.
   aiotools.start_server(worker_main, num_workers=4)
