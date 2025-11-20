from prometheus_client import Counter

FETCHES = Counter('cache_fetches_total',
    'Fetches from the cache.',
    labelnames=['cache'])

class MyCache(object):
    def __init__(self, name):
        self._fetches = FETCHES.labels(name)
        self._cache = {}
    def fetch(self, item):
        self._fetches.inc()
        return self._cache.get(item)
        def store(self, item, value):
        self._cache[item] = value
