from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = f"""
        <body>
        <h1>Hello, {name}</h1>
        <div>ABC</div><div>ABC</div>
        <span>ABC</span><span>ABC</span>
        </body>
    """
    return web.Response(text=text, content_type='text/html')


app = web.Application()
app.add_routes([web.get('/', handle)])


if __name__ == '__main__':
    web.run_app(app)