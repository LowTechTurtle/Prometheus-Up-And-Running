from prometheus_client import make_wsgi_app
from wsgiref.simple_server import make_server
from prometheus_client import Counter

metrics_app = make_wsgi_app()
REQUESTS = Counter('hello_worlds_total',
'Hello Worlds requested.')

def my_app(environ, start_fn):
    if environ['PATH_INFO'] == '/metrics':
        return metrics_app(environ, start_fn)
    start_fn('200 OK', [])
    REQUESTS.inc()
    return [b'Hello World']

if __name__ == '__main__':
    httpd = make_server('', 8000, my_app)
    httpd.serve_forever()
