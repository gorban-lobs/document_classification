from aiohttp import web

from routes import set_routes


app = web.Application()
routes = set_routes()
app.add_routes(routes)


if __name__ == '__main__':
    web.run_app(app)
