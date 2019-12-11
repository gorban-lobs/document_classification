from aiohttp import web


def get_html(file_name):
    with open(file_name, 'r') as html_file:
        html_template = html_file.read()
    return html_template


async def handler(request):
    params = request.rel_url.query
    if params:
        print(params)
    text = get_html('main_page.html')
    return web.Response(text=text, content_type='text/html')