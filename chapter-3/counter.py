import http.server
import prometheus_client
import random

REQUESTS = prometheus_client.Counter('hello_worlds_total',
'Hello Worlds requested.')
EXCEPTIONS = prometheus_client.Counter('hello_worlds_exceptions_total',
'Exceptions serving Hello World.')
SALES = prometheus_client.Counter("hello-worlds_sales_dollars_total", "dollars made by saying hello world")


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        with EXCEPTIONS.count_exceptions():
            if random.random() < 0.5:
                raise Exception
        dollars = random.random()
        SALES.inc(dollars)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"hello world")


if __name__ == "__main__":
    prometheus_client.start_http_server(8000)
    server = http.server.HTTPServer(("localhost", 8001), MyHandler)
    server.serve_forever()