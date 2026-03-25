from functools import wraps


class CacheDecorator:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __get__(self, instance, owner):
        # превращаем в bound method
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))

            if key in self.cache:
                print("From cache")
                return self.cache[key]

            print("Calculating...")
            result = self.func(instance, *args, **kwargs)
            self.cache[key] = result
            return result

        return wrapper