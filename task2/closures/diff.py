def diff():
    prev = None

    def inner(x):
        nonlocal prev
        if prev is None:
            prev = x
            return 0
        result = x - prev
        prev = x
        return result

    return inner