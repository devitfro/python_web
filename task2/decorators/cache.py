def cache(func):
    _cache = {}

    def wrapper(*args):
        if args in _cache:
            print("from cache")
            return _cache[args]

        print("calculating...")
        result = func(*args)
        _cache[args] = result
        return result

    return wrapper