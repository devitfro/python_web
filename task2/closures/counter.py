def count_args():
    counter = {}

    def inner(x):
        counter[x] = counter.get(x, 0) + 1
        return counter

    return inner