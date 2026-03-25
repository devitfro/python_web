def factorials():
    n = 1
    fact = 1
    while True:
        fact *= n
        yield fact
        n += 1