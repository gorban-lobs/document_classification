from aiohttp import web

from handlers import get_start_page


def set_routes():
    return [
        web.get('/', get_start_page),

    ]