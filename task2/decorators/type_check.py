def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for arg, t in zip(args, types):
                if not isinstance(arg, t):
                    raise TypeError(f"Expected {t}, got {type(arg)}")
            return func(*args)
        return wrapper
    return decorator