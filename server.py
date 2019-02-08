from aiohttp import web
import asyncio

routes = web.RouteTableDef()

log = 0

@routes.get('/')
async def normal_handler(request):
    global log
    print ("The log is ",log)
    msg = "Hellow the log is "
    num = str(log)
    msg = msg + num
    return web.Response(text=msg)

async def display_date():
    while True:
        global log
        log += 1
        await asyncio.sleep(1)

app = web.Application()
app.add_routes(routes)

loop = asyncio.get_event_loop()

future = loop.create_task(display_date())

web.run_app(app)
