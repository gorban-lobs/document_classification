from aiohttp import web

from routes import set_routes
from classifier import MultiClassifier
from sklearn.datasets import fetch_20newsgroups


app = web.Application()
routes = set_routes()
app.add_routes(routes)
train_dataset = fetch_20newsgroups(subset='train',
                                   remove=('headers', 'footers', 'quotes'))
app['multiclassifier'] = MultiClassifier(train_dataset.data,
                                         train_dataset.target,
                                         train_dataset.target_names)


if __name__ == '__main__':
    web.run_app(app)
