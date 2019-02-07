from aiohttp import web
routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    print("!!!")
    return web.Response(text="Hello, world")

@routes.get('/test')
async def hello(request):
    print("@@@")
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes(routes)
web.run_app(app)
