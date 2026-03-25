def limit_calls(n):
    count = 0

    def wrapper():
        nonlocal count
        if count >= n:
            raise Exception("Limit reached")
        count += 1
        return "OK"

    return wrapper