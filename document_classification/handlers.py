from aiohttp import web


def get_html(file_name):
    with open(file_name, 'r') as html_file:
        html_template = html_file.read()
    return html_template


async def handler(request):
    page_html = get_html('main_page.html')
    classifier_type = request.rel_url.query.get('type', None)
    text = request.rel_url.query.get('text', '')
    if classifier_type and text:
        result = request.app['multiclassifier'].classify_text(text,
                                                              classifier_type)
    else:
        result = 'Текст не введен или не выбран тип классификатора'
    page_html = page_html.format(input_text=text, result=result)
    return web.Response(text=page_html, content_type='text/html')