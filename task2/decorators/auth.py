def auth(func):
    def wrapper(user, *args):
        if not user.get("is_auth"):
            raise PermissionError("User not authorized")
        return func(user, *args)
    return wrapper