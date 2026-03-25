def checker(lst):
    def inner(x):
        return x in lst
    return inner