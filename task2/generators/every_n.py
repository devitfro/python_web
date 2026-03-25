def every_n(lst, n):
    for i in range(n - 1, len(lst), n):
        yield lst[i]