from aiohttp import web

from handlers import handler

def set_routes():
    return [
        web.get('/', handler),
    ]
