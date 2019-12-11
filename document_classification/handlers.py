from aiohttp import web


async def get_start_page(request):
    name = request.match_info.get('name', 'Anonymous')
    text = f"""
        <body>
        <h1>Hello, {name}</h1>
        <div>ABC</div>
        </body>
    """
    return web.Response(text=text, content_type='text/html')