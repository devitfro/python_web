def template(pattern):
    def formatter(*args):
        return pattern.format(*args)
    return formatter